"""
Write a function learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs) that adjusts the weights and bias by iterating through the training data and applying the perceptron learning rule. The function must return a pair (2-tuple) where the first element is the vector (list) of adjusted weights and second argument is the adjusted bias. The parameters of the function are:

weights: an array (list) of initial weights of length n
bias: a scalar number which is the initial bias
training_examples: a list of training examples where each example is a pair. The first element of the pair is a vector (tuple) of length n. The second element of the pair is an integer which is either 0 or 1 representing the negative or positive class correspondingly.
learning_rate: a positive number representing eta in the learning equations of perceptron.
max_epochs: the maximum number of times the learner is allowed to iterate through all the training examples.
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


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    cur_weights = weights[:]
    cur_bias = bias
    for i in range(max_epochs):
        for example in training_examples:
            perceptron = construct_perceptron(cur_weights, cur_bias)
            y = perceptron(example[0])
            w1 = cur_weights[0] + learning_rate * example[0][0] * (example[1] - y)
            w2 = cur_weights[1] + learning_rate * example[0][1] * (example[1] - y)
            cur_weights[0] = w1
            cur_weights[1] = w2
            cur_bias = cur_bias + learning_rate * (example[1] - y)
    return cur_weights, cur_bias


def main():
    print('test 1')
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 0),
      ((1, 0), 0),
      ((1, 1), 1),
      ]
    max_epochs = 50
    
    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")
    
    perceptron = construct_perceptron(weights, bias)
    
    print(perceptron((0,0)))
    print(perceptron((0,1)))
    print(perceptron((1,0)))
    print(perceptron((1,1)))
    print(perceptron((2,2)))
    print(perceptron((-3,-3)))
    print(perceptron((3,-1)))
    
    print()
    print('test 2')
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 1),
      ((1, 0), 1),
      ((1, 1), 0),
      ]
    max_epochs = 50
    
    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")    

if __name__ == '__main__':
    main()