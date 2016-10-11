import bandits
import bern_bandit
import egreedy
import ucb
import IPython
import thompson
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':



    trials = 100


    plays = 300
    samples = 20
    
    rewards1 = np.zeros((trials, plays))
    rewards2 = np.zeros((trials, plays))
    rewards3 = np.zeros((trials, plays))

    optimal_rewards = np.zeros((trials, plays))


    #env = bern_bandit.BernBandits()
    for t in range(trials):
        #env = bandits.Bandits()
        env = bern_bandit.BernBandits()        
        strat1 = egreedy.eGreedy(env.n)
        strat2 = ucb.UCB(env.n)
        strat3 = thompson.Thompson(env.n)

        
        for i in range(plays):
            arm1 = strat1.action()
            arm2 = strat2.action()
            arm3 = strat3.action()
           
            r1 = env.pull(arm1)
            r2 = env.pull(arm2)
            r3 = env.pull(arm3)

            strat1.update(arm1, r1)
            strat2.update(arm2, r2)
            strat3.update(arm3, r3)

            best_arm1 = strat1.best_arm()
            best_arm2 = strat2.best_arm()
            best_arm3 = strat3.best_arm()
            #print "egreedy best arm: " + str(best_arm1)
            #print "ucb best arm: " + str(best_arm2)

            for s in range(samples):
                sample_r1 = env.pull(best_arm1)
                sample_r2 = env.pull(best_arm2)
                sample_r3 = env.pull(best_arm2)
                

                rewards1[t, i] += sample_r1 / float(samples)
                rewards2[t, i] += sample_r2 / float(samples)
                rewards3[t, i] += sample_r3 / float(samples)

        print "eGreedy:", best_arm1, "UCB:", best_arm2, "Thompson:", best_arm3
        print "Actual:", env.best_indices, "\n"
              

    average_reward1 = np.mean(rewards1, axis=0)
    average_reward2 = np.mean(rewards2, axis=0)
    average_reward3 = np.mean(rewards3, axis=0)



    fig, ax1 = plt.subplots()
    ax1.plot(average_reward1, linewidth=2)    
    ax1.plot(average_reward2, linewidth=2)
    ax1.plot(average_reward3, linewidth=2)
    ax1.legend(["e-Greedy", "UCB", "Thompson"], loc=4)
    plt.show()
