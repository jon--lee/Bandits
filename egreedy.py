import numpy as np

class eGreedy():

    def __init__(self, n):
        self.sample_counts = np.zeros(n)
        self.sample_sums = np.zeros(n)
        self.n = n
        self.eps = .1
        self.t = 0
        self.value = 0.0

    def update(self, arm, r):
        self.sample_counts[arm] += 1
        self.sample_sums[arm] += r
        self.value += r
        self.t += 1
        
        
        
    def action(self, greedy=False):
        rand = np.random.rand()
        if (greedy or rand > self.eps) and any(self.sample_sums):
            return self.best_arm()
        else:
            return np.random.randint(0, self.n)
        

    def best_arm(self):
        means = self.sample_sums / self.sample_counts
        best_i = 0
        for i in range(self.n):
            if self.sample_counts[best_i] > 0:
                if means[i] > means[best_i]:
                    best_i = i
        return best_i

