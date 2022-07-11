"""
Write a function posterior(prior, likelihood, observation) that returns the posterior probability of the class variable being true, given the observation; that is, it returns p(Class=true|observation). The argument observation is a tuple of n Booleans such that observation[i] is the observed value (True or False) for the input feature X[i]. The arguments prior and likelihood are as described above.

Notes

Example 8.35 in the textbook is relevant.
The model used in the test cases is according to this network. You can download and explore the model in the belief network applet.
"""
def posterior(prior, likelihood, observation):
    true = prior
    false = (1-prior)
    for i in range(len(observation)):
        if observation[i]:
            true *= likelihood[i][True]
            false *= likelihood[i][False]
        else:
            true *= 1 - likelihood[i][True]
            false *= 1 - likelihood[i][False]
    normal = true + false
    return true / normal

def main():
    print('test 1')
    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    
    observation = (True, True, True)
    
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))  
    
    print()
    print('test 2')
    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    
    observation = (True, False, True)
    
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))  
    
    print()
    print('test 3')
    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    
    observation = (False, False, True)
    
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))  
    
    print()
    print('test 4')
    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    
    observation = (False, False, False)
    
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))      
    
if __name__ == '__main__':
    main()