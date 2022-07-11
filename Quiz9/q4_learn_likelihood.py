"""
Write a function learn_likelihood(file_name, pseudo_count=0) that takes the file name of a training set (for the spam detection problem) and an optional pseudo-count parameter and returns a sequence of pairs of likelihood probabilities. As described in the representation of likelihood, the length of the returned sequence (list or tuple) must be 12. Each element in the sequence is a pair (tuple) of real numbers such that likelihood[i][False] is P(X[i]=true|Spam=false) and likelihood[i][True] is P(X[i]=true|Spam=true ).
"""
import csv
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
    
    print()
    print('test 5')
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
    print("\n".join([format(p1, ".5f") + "  " + format(p2, ".5f")
                     for p1, p2 in likelihood]))    

    
if __name__ == '__main__':
    main()