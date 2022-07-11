def posterior(prior, likelihood, observation):
    p = prior
    q = 1 - prior
    for i in range(len(likelihood)):
        if observation[i]:
            p *= likelihood[i][True]
            q *= likelihood[i][False]
        else:
            p *= 1 - likelihood[i][True]
            q *= 1 - likelihood[i][False]            
    norm = p + q
    return p / norm


def main():
    print('Test 1')
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
    
if __name__ == "__main__":
    main()