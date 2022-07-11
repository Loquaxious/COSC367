"""
Write a function accuracy(classifier, inputs, expected_outputs) that passes each input in the sequence of inputs to the given classifier function (e.g. a perceptron) and compares the predictions with the expected outputs. The function must return the accuracy of the classifier on the given data. Accuracy must be a number between 0 and 1 (inclusive).

Note: an important application of a metric such as accuracy is to see how a classifier (e.g. a spam filter) performs on unseen data. In this case, the inputs must be some data that it has not seen during training but has been labeled by humans.
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


def accuracy(classifier, inputs, expected_outputs):
    correct = 0
    for i in range(len(inputs)):
        if classifier(inputs[i]) == expected_outputs[i]:
            correct += 1
    return correct / len(inputs)


def main():
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]
    
    print(accuracy(perceptron, inputs, targets))

if __name__ == '__main__':
    main()