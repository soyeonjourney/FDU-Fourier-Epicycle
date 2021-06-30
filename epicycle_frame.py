import numpy as np


class EpicycleFrame:
    """Compute all epicycle's track at frame time t."""
    def __init__(self, ft, t):
        """
        :params:
            FT: Fourier Transform object
            t: frame time t
        :return:
            the epicycle drawing at frame time t
            circles: all pointers' loci, stored in a list
            lines: all pointers' current indications, stored in a list
            paintbrush: position of current paintbrush
        """
        self.ft = ft
        self.t = t
        self.order = self.ft.order
        self.coeffs = self.ft.coeffs
        self.amplitude = self.ft.amplitude

        # Frequency exponential terms at frame time t, as direction vectors
        # Sort them by the order 0, 1, -1, 2, -2, ..., order, -order
        exp_term = [np.exp(0)]
        for k in range(1, self.order+1):
            exp_term.extend([np.exp(2j * np.pi * k * self.t), np.exp(-2j * np.pi * k * self.t)])
        exp_term = np.array(exp_term)

        # Compute the position of every epicycle's pointer at frame time t
        # Simply use `coeffs * exp_term`
        self.pointer = self.coeffs * exp_term

        # Split into x and y coefficients
        self.pointer_x = np.real(self.pointer)
        self.pointer_y = np.imag(self.pointer)
        
        # Draw a circle to indicate the locus, stored in `self.circles` (list)
        # Draw a line to indicate the pointer, stored in `self.lines` (list)
        self.circles = []
        self.lines = []
        center_x, center_y = 0, 0
        theta = np.linspace(0, 2*np.pi, num=50)  # Take 50 sampling points

        for i, (pointer_x, pointer_y) in enumerate(zip(self.pointer_x, self.pointer_y)):
            self.circles.append([[center_x + self.amplitude[i] * np.cos(theta)],
                                [center_y + self.amplitude[i] * np.sin(theta)]])
            self.lines.append([[center_x, center_x + pointer_x],
                              [center_y, center_y + pointer_y]])
            # Center for next circle
            center_x, center_y = center_x + pointer_x, center_y + pointer_y
        
        # Center points now are used as paintbrush's position
        self.paintbrush = [center_x, center_y]
