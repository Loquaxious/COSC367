"""
Write a function learn_prior(file_name, pseudo_count=0) that takes the file name of the training set and an optional pseudo-count parameter and returns a real number that is the prior probability of spam being true. The parameter pseudo_count is a non-negative integer and it will be the same for all the attributes and all the values.

Notes

Pseudo-counts are described in the lecture notes and section 7.2.3 of the textbook.
Although you see high values of pseudo-count in some test cases, in practice small values are mostly used. 
"""
import csv
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
        print('test 5')
        prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
        print(format(prior, ".5f"))
        
        print()
        print('test 6')
        prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
        print(format(prior, ".5f"))
        
        print()
        print('test 7')
        prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
        print(format(prior, ".5f"))
        
if __name__ == '__main__':
        main()