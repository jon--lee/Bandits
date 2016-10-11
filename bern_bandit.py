import numpy as np
import random
class BernBandits():


    def __init__(self):
        self.n = 100
        self.ps = np.random.normal(.5, .25, self.n)
        #self.ps = np.random.rand(self.n) 
        self.best_arm = np.argmax(self.ps)
        self.best_indices = np.argsort(self.ps)[::-1]


    def pull(self, arm):
        r = random.random()
        if r < self.ps[arm]:
            return 1.0
        else:
            return 0.0
