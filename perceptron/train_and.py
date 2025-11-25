from perceptron import Perceptron
import numpy as np

# Creating input data
# x contains 4 samples, each with 2 features.
x = np.array([[0,0],[0,1],[1,0],[1,1]])
# Creating target labels
# These are the correct outputs of the AND gate.
y = np.array([0,0,0,1])

model = Perceptron(lr=0.1)
model.train(x,y)

# Testing the model
# This loops through all four input samples and prints predictions.
# Expected output after correct training should be
for sample in x:
    print(sample, "->", model.predict(sample))
