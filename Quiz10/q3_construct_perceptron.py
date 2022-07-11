"""
A perceptron is a function that takes a vector (list of numbers) of size n and returns 0 or 1 according to the definition of perceptron.

Write a function construct_perceptron(weights, bias) where weights is a vector (list of numbers) of of length n and bias is a scalar number and returns the corresponding perceptron function.
"""
def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        n = len(weights)
        a = bias
        for i in range(n):
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

if __name__ == '__main__':
    main()