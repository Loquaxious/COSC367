import csv

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


def learn_prior(filename, pseudo_count=0):
    with open(filename) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    true_count = 0   
    for row in training_examples:
        if row[-1] == '1':
            true_count += 1
    
    return (true_count+pseudo_count) / (len(training_examples)-1 + (2*pseudo_count))


def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    pairs = []
    for col in range(len(training_examples[0]) - 1):
        spam_true_count = 0
        true_count = 0
        false_count = 0
        for row in range(len(training_examples)):
            if training_examples[row][-1] == '1':
                spam_true_count += 1
                if training_examples[row][col] == '1':
                    true_count += 1
            else:
                if training_examples[row][col] == '1':
                    false_count += 1
        p_true = (true_count + pseudo_count) / (spam_true_count + (2*pseudo_count))
        p_false = (false_count + pseudo_count) / (((len(training_examples)-1)-spam_true_count) + (2*pseudo_count))
        pairs.append((p_false, p_true))
    return pairs


def nb_classify(prior, likelihood, input_vector):
    p = posterior(prior, likelihood, input_vector)
    if p >= 0.5:
        return ('Spam', p)
    else:
        return ('Not Spam', 1 - p)


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