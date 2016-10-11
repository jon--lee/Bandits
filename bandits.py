import numpy as np

class Bandits():

    def __init__(self):
        self.n = 20
        #sigmas = np.random.randint(1, 2, self.n)
        sigmas = np.zeros(self.n) + .25
        mus = np.random.normal(.5, .25, self.n)
        #sigmas = np.random.rand(self.n) * 5
        #mus = np.random.normal(5, 4, self.n)

        self.best_arm = np.argmax(mus)
        self.sigmas = sigmas
        self.mus = mus
        
    def pull(self, arm):
        return np.random.normal(self.mus[arm], self.sigmas[arm])


if __name__ == '__main__':
    bandit = Bandits()
    

    
        
