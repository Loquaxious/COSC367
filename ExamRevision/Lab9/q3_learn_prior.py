import csv

def learn_prior(filename, pseudo_count=0):
    with open(filename) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    true_count = 0   
    for row in training_examples:
        if row[-1] == '1':
            true_count += 1
    
    return (true_count+pseudo_count) / (len(training_examples)-1 + (2*pseudo_count))


def main():
    print('test 1')
    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of spam is {:.5f}.".format(prior))

    print()
    print('test 2')    
    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of not spam is {:.5f}.".format(1 - prior))
    
    print()
    print('test 3')    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
    print(format(prior, ".5f"))
    
    print()
    print('test 4')    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
    print(format(prior, ".5f"))
    
    print()
    print('test 4')    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
    print(format(prior, ".5f"))
    
    print()
    print('test 5')    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
    print(format(prior, ".5f"))
    
    print()
    print('test 6')    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
    print(format(prior, ".5f"))    
    
if __name__ == '__main__':
    main()