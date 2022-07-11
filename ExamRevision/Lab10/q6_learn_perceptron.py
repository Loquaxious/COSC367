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


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    for _ in range(max_epochs):
        for i in range(len(training_examples)):
            a = bias + weights[0] * training_examples[i][0][0] + weights[1] * \
                training_examples[i][0][1]
            if a >= 0:
                y = 1
            else:
                y = 0
            
            weights[0] = weights[0] + learning_rate * training_examples[i][0][0] \
                * (training_examples[i][1] - y)
            weights[1] = weights[1] + learning_rate * training_examples[i][0][1] \
                * (training_examples[i][1] - y)
            bias = bias + learning_rate * (training_examples[i][1] - y)
    return (weights, bias)


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