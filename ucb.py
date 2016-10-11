import numpy as np

class UCB():

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
        return self.next_arm()
        

    def next_arm(self):
        #for i in range(self.n):
        #    if self.sample_counts[i] == 0:
        #        return i
        means = self.sample_sums / self.sample_counts
        
        numerator = 2 * np.log([self.t]*self.n) 
        denominator = np.array(self.sample_counts)
        bound_term = np.sqrt(numerator / denominator)
        bounds = bound_term + means
        
        return np.argmax(bounds)

    def best_arm(self):
        means = self.sample_sums / self.sample_counts
        best_i = 0
        for i in range(self.n):
            if self.sample_counts[best_i] > 0:
                if means[i] > means[best_i]:
                    best_i = i
        return best_i



    """def best_arm(self):
        n_arms = len(self.sample_counts)
        for arm in range(self.n):
            if self.sample_counts[arm] == 0:
                return arm

        ucb_values = [0.0 for arm in range(self.n)]
        total_counts = self.t
        for arm in range(self.n):
            bonus = np.sqrt((2 * np.log(total_counts)) / float(self.sample_counts[arm]))
            ucb_values[arm] = self.sample_sums[arm] / float(self.sample_counts[arm]) + bonus
        return np.argmax(ucb_values)
"""
    
