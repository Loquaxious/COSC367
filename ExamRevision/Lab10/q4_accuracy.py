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


def accuracy(classifier, inputs, expected_outputs):
    correct = 0
    for i in range(len(inputs)):
        a = classifier(inputs[i])
        if a == expected_outputs[i]:
            correct+=1
    return correct / len(inputs)


def main():
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]
    
    print(accuracy(perceptron, inputs, targets))   
    
if __name__ == '__main__':
    main()