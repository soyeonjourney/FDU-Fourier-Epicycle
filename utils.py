import numpy as np
from scipy.interpolate import CubicSpline
from scipy.fftpack import fft  # built-in fft


# 1.  Using DFT
#     Return c_k series (k = 0, 1, -1, 2, -2, ..., order, -order)
def coeffs_mydft(x, order):
    """Use DFT."""
    coeffs = [my_dft(x, 0)]
    for k in range(1, order+1):
        coeffs.extend([my_dft(x, k), my_dft(x, -k)])
    coeffs = np.array(coeffs) / len(coeffs)
    return coeffs


# 2. Using linear interpolation & power-2 FFT
#    Return c_k series (k = 0, 1, -1, 2, -2, ..., order, -order)
def coeffs_myfft(x, order):
    """Use linear interpolation & power-2 FFT."""
    # Linear interpolation
    x = np.asarray(x)
    N = np.power(2, int(np.rint(np.log2(x.shape[0]))))
    t = np.linspace(0, 1, num=x.shape[0])
    t_new = np.linspace(0, 1, num=N)
    x_new = lin_interp(t_new, t, x)

    # Power-2 FFT
    coeffs = my_fft_pow_two(x_new) / len(x_new)
    coeffs = sort_coeffs(coeffs, N=2*order+1)
    return coeffs


# 3. Using cubic interpolation & power-2 FFT
#    Return c_k series (k = 0, 1, -1, 2, -2, ..., order, -order)
def coeffs_myfft_plus(x, order):
    """Use cubic spline interpolation & power-2 FFT."""
    x = np.asarray(x)
    N = np.power(2, int(np.rint(np.log2(x.shape[0]))))
    t = np.linspace(0, 1, num=x.shape[0])
    t_new = np.linspace(0, 1, num=N)
    # x_new = cubic_spline_prd(t_new, t, x)
    cs = CubicSpline(t, x)
    x_new = cs(t_new)

    # Power-2 FFT
    coeffs = my_fft_pow_two(x_new) / len(x_new)
    coeffs = sort_coeffs(coeffs, N=2*order+1)
    return coeffs


# 4. Using built-in FFT
#    Return c_k series (k = 0, 1, -1, 2, -2, ..., order, -order)
def coeffs_fft(x, order):
    """Use built-in FFT."""
    coeffs = sort_coeffs(fft(x), N=2*order+1) / len(x)
    return coeffs


# Real number convert to complex number
def r2c(x, y):
    """return: x + y * j"""
    x, y = np.asarray(x), np.asarray(y)
    return x + 1j * y


# DFT implementation
def my_dft(x, k):
    """Return k-th coeff for DFT."""
    x = np.asarray(x)
    N = x.shape[0]
    exp_term = np.exp(-2j * np.pi * k * np.arange(N) / N)
    coeff = np.dot(exp_term, x)
    return coeff


# Power-2 FFT implementation
def my_fft_pow_two(x):
    """Compute power-2 FFT using iteration."""
    x = np.asarray(x)
    N = x.shape[0]
    x_even = x[::2]
    x_odd = x[1::2]

    if N >= 4:
        coeff_even = my_fft_pow_two(x_even)
        coeff_odd = my_fft_pow_two(x_odd)
        coeff_odd = coeff_odd * np.exp(-2j * np.pi * np.arange(int(N/2)) / N)
        coeffs = np.concatenate([coeff_even + coeff_odd, coeff_even - coeff_odd])
    else:
        coeffs = np.dot(np.array([[1, 1], [1, -1]]), x)
    return coeffs


# Linear interpolation
def lin_interp(x, xp, fp):
    """Linear interplation."""
    x, xp, fp = np.asarray(x), np.asarray(xp), np.asarray(fp)
    f_list = []
    for xx in x:
        idx = np.argmax(xp>xx)
        f_list.append(
            (fp[idx-1]*(xp[idx]-xx) + fp[idx]*(xx-xp[idx-1])) / (xp[idx]-xp[idx-1]))
    return np.array(f_list)


# Periodic cubic spline interpolation
def cubic_spline_prd(x, xp, fp):
    """Periodic cubic spline interpolation by MATLAB scripts."""
    # To be done
    pass


# Sort the coefficients in order 0, 1, -1, 2, -2, ..., order, -order
def sort_coeffs(coeffs, N=None):
    """Sort coefficients in order 0, 1, -1, 2, -2, ..., order, -order."""
    coeffs = np.asarray(coeffs)
    if N is None:
        N = coeffs.shape[0]
    sorted_list = [coeffs[0]]
    for i in range(1, int((N+1)/2)):
        sorted_list.extend([coeffs[i], coeffs[-i]])
    if N % 2 == 0:
        sorted_list.append(coeffs[int(N/2)])
    return np.array(sorted_list)
