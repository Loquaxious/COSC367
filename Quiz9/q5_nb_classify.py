"""
Write a function nb_classify(prior, likelihood, input_vector) that takes the learnt prior and likelihood probabilities and classifies an (unseen) input vector. The input vector will be a tuple of 12 integers (each 0 or 1) corresponding to attributes X1 to X12. The function should return a pair (tuple) where the first element is either "Spam" or "Not Spam" and the second element is the certainty. The certainty is the (posterior) probability of spam when the instance is classified as spam, or the probability of 'not-spam' otherwise. If spam and 'not spam' are equally likely (i.e. p=0.5) then choose 'not spam'.

This is a very simple function to implement as it only wraps the posterior function developed earlier.

Supply the following functions you developed earlier: learn_prior and learn_likelihood. Also include import statements and any other function that you may be using (e.g. posterior).
"""
import csv
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


def learn_prior(file_name, pseudo_count=0):
        with open(file_name) as in_file:
                data = [tuple(row) for row in csv.reader(in_file)]
        true_count = 0
        false_count = 0
        for i in range(1, len(data)):
                if data[i][-1] == '1':
                        true_count += 1
                else:
                        false_count += 1
        total_count = true_count + false_count
        return (true_count + pseudo_count) / (total_count + (2*pseudo_count))
    
    
def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as infile:
        data = [tuple(row) for row in csv.reader(infile)]
    likelihood = []
    for i in range(12):
        t_count = 0 #True Count
        f_count = 0 #False Count
        ttlt_count = 0 #Total True Count
        ttlf_count = 0 #Total False Count        
        for j in range(1, len(data)):
            if data[j][-1] == '1':
                if data[j][i] == '1':
                    t_count += 1
                ttlt_count += 1
            else:
                if data[j][i] == '1':
                    f_count += 1
                ttlf_count += 1
        likelihood.append(((f_count + pseudo_count) / (ttlf_count + (2*pseudo_count)),
                          (t_count + pseudo_count) / (ttlt_count + (2*pseudo_count))))
    return likelihood


def nb_classify(prior, likelihood, input_vector):
    p = posterior(prior, likelihood, input_vector)
    if p <= 0.5:
        return (("Not Spam", 1 - p))
    else:
        return (("Spam", p))

def main():
    print('test 1')
    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")
    
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    
    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]
    
    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))
    
    print()
    print('test 2')
    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
    
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    
    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]
    
    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))
if __name__ == '__main__':
    main()