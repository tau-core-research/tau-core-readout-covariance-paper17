import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

def normalize(field):
    field = field - np.mean(field)
    std = np.std(field)
    return field if std == 0 else field / std

def generate_anisotropic_field(n, ell_parallel, ell_perp, rng):
    kx = np.fft.fftfreq(n) * 2.0 * np.pi
    ky = np.fft.fftfreq(n) * 2.0 * np.pi
    kx_grid, ky_grid = np.meshgrid(kx, ky, indexing="ij")
    spectrum = np.exp(-0.5 * ((kx_grid * ell_parallel) ** 2 + (ky_grid * ell_perp) ** 2))
    white = rng.normal(size=(n, n))
    field_fft = np.fft.fft2(white) * np.sqrt(spectrum)
    return normalize(np.real(np.fft.ifft2(field_fft)))

def generate_parent(n, ell_parallel, ell_perp, rng):
    p_plus = generate_anisotropic_field(n, ell_parallel, ell_perp, rng)
    p_minus_base = generate_anisotropic_field(n, ell_parallel, ell_perp, rng)
    p_minus = normalize(0.5 * p_plus + 0.5 * p_minus_base)
    return p_plus, p_minus

def make_readout(p_plus, p_minus, r):
    return normalize(p_plus + r * p_minus)

def make_lensing_residual(x, sigma, noise_level, rng):
    field = normalize(gaussian_filter(x, sigma=sigma))
    return normalize(field + noise_level * rng.normal(size=field.shape))

def filament_score(field, hessian_sigma=1.0, ridge_scale=1.0):
    f_xx = gaussian_filter(field, sigma=hessian_sigma, order=(2, 0))
    f_yy = gaussian_filter(field, sigma=hessian_sigma, order=(0, 2))
    f_xy = gaussian_filter(field, sigma=hessian_sigma, order=(1, 1))
    trace = f_xx + f_yy
    det_term = np.sqrt((f_xx - f_yy) ** 2 + 4.0 * f_xy ** 2)
    lambda1 = 0.5 * (trace - det_term)
    lambda2 = 0.5 * (trace + det_term)
    score = np.maximum(0.0, -lambda1) * np.exp(-(lambda2 ** 2) / (ridge_scale ** 2))
    return normalize(score)

def make_morphology_residual(x, sigma, noise_level, rng):
    field = normalize(gaussian_filter(x, sigma=sigma))
    field = normalize(field + noise_level * rng.normal(size=field.shape))
    return filament_score(field)

def cross_corr_axis(a, b, max_lag, axis):
    a = normalize(a)
    b = normalize(b)
    return np.array([np.mean(a * np.roll(b, shift=lag, axis=axis)) for lag in range(1, max_lag + 1)])

def correlation_scores(delta_l, delta_f, max_lag):
    c_parallel = cross_corr_axis(delta_l, delta_f, max_lag=max_lag, axis=0)
    c_perp = cross_corr_axis(delta_l, delta_f, max_lag=max_lag, axis=1)
    strength = np.sum(np.abs(c_parallel)) + np.sum(np.abs(c_perp))
    anisotropy = np.sum(np.abs(c_parallel)) / (np.sum(np.abs(c_perp)) + 1e-12)
    return c_parallel, c_perp, strength, anisotropy

def phase_randomize(field, rng):
    fft = np.fft.fft2(field)
    amplitude = np.abs(fft)
    random_phase = rng.uniform(0, 2.0 * np.pi, size=field.shape)
    return normalize(np.real(np.fft.ifft2(amplitude * np.exp(1j * random_phase))))

def run_surrogates(delta_l, delta_f, max_lag, rng, num_surrogates):
    strengths, anisotropies = [], []
    for _ in range(num_surrogates):
        choice = rng.integers(0, 3)
        if choice == 0:
            surrogate_f = np.rot90(delta_f)
        elif choice == 1:
            surrogate_f = phase_randomize(delta_f, rng)
        else:
            surrogate_f = normalize(rng.permutation(delta_f.ravel()).reshape(delta_f.shape))
        _, _, strength, anisotropy = correlation_scores(delta_l, surrogate_f, max_lag)
        strengths.append(strength)
        anisotropies.append(anisotropy)
    return np.array(strengths), np.array(anisotropies)

def z_score(value, surrogate_values):
    return (value - np.mean(surrogate_values)) / (np.std(surrogate_values) + 1e-12)

def run_world(shared_parent=True, seed=42):
    rng = np.random.default_rng(seed)
    n = 128
    ell_parallel = 20.0
    ell_perp = 4.0
    sigma_lensing = 3.0
    sigma_morphology = 2.0
    r_lensing = 0.2
    r_morphology = 0.6
    noise = 0.5
    max_lag = 30
    num_surrogates = 100

    if shared_parent:
        p_plus, p_minus = generate_parent(n, ell_parallel, ell_perp, rng)
        x_l = make_readout(p_plus, p_minus, r_lensing)
        x_f = make_readout(p_plus, p_minus, r_morphology)
    else:
        p_l_plus, p_l_minus = generate_parent(n, ell_parallel, ell_perp, rng)
        p_f_plus, p_f_minus = generate_parent(n, ell_parallel, ell_perp, rng)
        x_l = make_readout(p_l_plus, p_l_minus, r_lensing)
        x_f = make_readout(p_f_plus, p_f_minus, r_morphology)

    delta_l = make_lensing_residual(x_l, sigma_lensing, noise, rng)
    delta_f = make_morphology_residual(x_f, sigma_morphology, noise, rng)
    c_parallel, c_perp, strength, anisotropy = correlation_scores(delta_l, delta_f, max_lag)
    s_strengths, s_anis = run_surrogates(delta_l, delta_f, max_lag, rng, num_surrogates)

    return {
        "strength": strength,
        "anisotropy": anisotropy,
        "z_strength": z_score(strength, s_strengths),
        "z_anisotropy": z_score(anisotropy, s_anis),
        "c_parallel": c_parallel,
        "c_perp": c_perp,
    }

if __name__ == "__main__":
    tau = run_world(shared_parent=True, seed=42)
    null = run_world(shared_parent=False, seed=10042)

    print("Tau-like shared-parent world")
    print(tau)
    print()
    print("Null independent-parent world")
    print(null)
