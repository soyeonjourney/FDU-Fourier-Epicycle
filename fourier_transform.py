import numpy as np
from utils import real2complex, coeffs_mydft, coeffs_myfft, coeffs_myfft_plus, coeffs_fft


class FourierTransform:
    """Compute fourier coefficients from -order to order."""
    def __init__(self, x_list, y_list, order, mode='fft'):
        """
        :params:
            x_list: sampled x-coordinate data list of a 2-D drawing
            y_list: sampled y-coordinate data list of a 2-D drawing
            order: order of fourier coeffs, `2 * order + 1` <= num of sampling points
        :return:
            coeffs: coefficients of frequency exponential terms,
                   (c_0, c_1, c_-1, ..., c_order, c_-order)
                   gives infomation about amplitude & initial phase
            amplitude: amplitudes of all circles,
                       (r_0, r_1, r_-1, ..., r_order, r_-order)
        """
        self.order = order
        self.mode = mode
        self.x_array = np.asarray(x_list, dtype=float)
        self.y_array = np.asarray(y_list, dtype=float)

        # Sets the first and last points to their average
        x_avrg = np.mean([self.x_array[0], self.x_array[-1]])
        y_avrg = np.mean([self.y_array[0], self.y_array[-1]])
        self.x_array[0], self.x_array[-1] = x_avrg, x_avrg
        self.y_array[0], self.y_array[-1] = y_avrg, y_avrg

        # 2-D coordinate to 1-D complex number
        self.f_array = real2complex(self.x_array, self.y_array)

        # Compute coeffs with different methods
        if self.mode == 'fft':
            self.coeffs = coeffs_fft(self.f_array, order)
        elif self.mode == 'mydft':
            self.coeffs = coeffs_mydft(self.f_array, order)
        elif self.mode == 'myfft':
            self.coeffs = coeffs_myfft(self.f_array, order)
        elif self.mode == 'myfftplus':
            self.coeffs = coeffs_myfft_plus(self.f_array, order)
        else:
            raise Exception("Undefined mode.")
        
        # Compute amplitude of all circles
        self.amplitude = np.abs(self.coeffs)
