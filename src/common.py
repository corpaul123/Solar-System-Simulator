import numpy as np
import matplotlib.pyplot as plt

class System:
    def __init__(
            self, num_particles: int, x: np.ndarray, v: np.ndarray, m: np.ndarray, G: float
    ) -> None:
        self.num_particles = num_particles
        self.x = x
        self.v = v
        self.m = m
        self.G = G

    def center_of_mass_correction(self) -> None:
        dim = self.x.shape[1]
        x_cm = np.zeros(dim)
        v_cm = np.zeros(dim)
        M = 0.0
        for i in range(self.num_particles):
            x_cm += self.m[i] * self.x[i]
            v_cm += self.m[i] * self.v[i]
            M += self.m[i]
        
        x_cm /= M
        v_cm /= M
        self.x -= x_cm
        self.v -= v_cm

    def compute_force(self):
        print("computing forces")