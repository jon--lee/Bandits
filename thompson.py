import numpy as np
import random
class Thompson():

    def __init__(self, n):
        self.sample_counts = np.ones(n)
        self.sample_sums = np.zeros(n)
        self.n = n
        self.t = self.n
        self.value = 0.0
    
        self.alpha = 1
        self.beta = 1

        self.succ = np.zeros(n)
        self.fail = np.zeros(n)

    def update(self, arm, r):
        self.sample_counts[arm] += 1
        self.sample_sums[arm] += r
        self.value += r
        self.t += 1

        if r == 0:
            self.fail[arm] += 1
        elif r== 1:
            self.succ[arm] += 0
        else:
            raise NotImplementedError

    def action(self):
        theta = np.zeros(self.n)
        for i in range(self.n):
            theta[i] = np.random.beta(self.succ[i] + self.alpha, self.fail[i] + self.beta)
        theta_max = np.argmax(theta)
        return theta_max
        #args = np.argwhere(theta == np.amax(theta))
        #return random.choice(args.flatten().tolist())
    
    def best_arm(self):
        means = self.sample_sums / self.sample_counts
        best_i = 0
        for i in range(self.n):
            if self.sample_counts[best_i] > 0:
                if means[i] > means[best_i]:
                    best_i = i
        return best_i

        
        
