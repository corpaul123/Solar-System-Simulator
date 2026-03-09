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