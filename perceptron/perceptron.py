import numpy as np

class Perceptron:
    def __init__(self, lr=0.1):
        """
        Defines a Perceptron object (a single artificial neuron)

        :param lr: learning rate
        """
        # Saves the learning rate.
        # This controls how much the weights update during training.
        self.lr = lr
        # Creates two random weights, one for each input feature.
        # Example: [0.41, -0.12]
        self.weights = np.random.randn(2)
        # Creates a random bias term.
        # Example: 0.8
        self.bias = np.random.randn()

    @staticmethod
    def activation(inputs_dot):
        """
        This is a step function.
        If the neuron's internal value is ≥ 0, output 1
        Otherwise output 0
        This is how early perceptrons decide TRUE/FALSE.

        :param inputs_dot: Neuron's internal value
        """
        return 1 if inputs_dot >= 0 else 0

    def predict(self, inputs):
        """
        Dot product
        Adds the bias term
        Passes the result into the activation function
        :param inputs:
            sample:
                inputs = [x1, x2]
                weights = [w1, w2]

                dot = x1*w1 + x2*w2

        :return:  gives 0 or 1
        """
        inputs_dot_ = np.dot(inputs, self.weights)+ self.bias
        return self.activation(inputs_dot_)

    def train(self, inputs, targets, epochs=20):
        """
        :param inputs:
        :param targets:
        :param epochs:
        :return:
        """
        # Runs the training multiple times over all data.
        # One "epoch" = one full pass over the dataset.
        for epoch in range(epochs):
            # input_ → e.g., [1, 0]
            # target_ → e.g., 1
            for input_, target_ in zip(inputs, targets):
                # The perceptron guesses 0 or 1
                pred = self.predict(input_)
                # If the model is right → error = 0
                # If it is wrong → error = +1 or -1
                err =  target_ -pred
                self.weights += self.lr * err * input_
                self.bias += self.lr * err
