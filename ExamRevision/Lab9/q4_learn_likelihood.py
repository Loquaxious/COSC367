import csv

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


def main():
    print('test 1')
    likelihood = learn_likelihood("spam-labelled.csv")
    print(len(likelihood))
    print([len(item) for item in likelihood])
    
    print()
    print('test 2')
    likelihood = learn_likelihood("spam-labelled.csv")
    
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))
    
    print()
    print('test 3')
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
    
    print("With Laplacian smoothing:")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True])) 
    
if __name__ == '__main__':
    main()