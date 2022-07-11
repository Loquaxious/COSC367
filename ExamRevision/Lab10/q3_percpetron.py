def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        a = bias
        for i in range(len(weights)):
            a += weights[i] * input[i] 
        if a >= 0:
            return 1
        else:
            return 0
    
    return perceptron # this line is fine

def main():
    weights = [2, -4]
    bias = 0
    perceptron = construct_perceptron(weights, bias)
    
    print(perceptron([1, 1]))
    print(perceptron([2, 1]))
    print(perceptron([3, 1]))
    print(perceptron([-1, -1]))
    
    print()
    weights = [3, 5]
    bias = 1
    perceptron = construct_perceptron(weights, bias)
    
    print(perceptron([0, 0]))
    print(perceptron([1, -1]))
    print(perceptron([-1, 1]))    
    
if __name__ == '__main__':
    main()