# Neural Networks Basics — Perceptron & XOR MLP

## Project Overview
This project demonstrates the fundamentals of neural networks using Python.  
It covers:
- Implementing a Perceptron from scratch with NumPy  
- Training Perceptron on AND / OR logic gates  
- Explaining why Perceptron fails for XOR  
- Solving XOR using a Multi-Layer Perceptron (MLP) with scikit-learn

---

## Project Architecture


**Key Points:**
- `perceptron/` contains all Perceptron code and training scripts.
- `xor-mlp/` contains a simple MLP to solve XOR.
- `reports/` explains neural network theory, Perceptron limitations, and MLP solution.
- `tests/` includes automated testing of predictions.

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/neural-networks-basics.git
cd neural-networks-basics

Install dependencies:

pip install -r requirements.txt


Run Perceptron on AND:

python perceptron/train_and.py


Run Perceptron on OR:

python perceptron/train_or.py


Run MLP for XOR:

python xor-mlp/mlp_xor.py

Example Outputs

Perceptron AND:

AND predictions:
[0 0] => 0
[0 1] => 0
[1 0] => 0
[1 1] => 1


Perceptron OR:

OR predictions:
[0 0] => 0
[0 1] => 1
[1 0] => 1
[1 1] => 1


MLP XOR:

XOR predictions: [0 1 1 0]

Notes

Learning rate (lr) controls how fast the model updates weights during training.

Perceptron can only solve linearly separable problems (like AND/OR).

XOR requires a multi-layer network because it is not linearly separable.




---

If you want, I can **also add a small ASCII diagram showing how Perceptron vs MLP solves XOR**—that makes the README visually stronger for GitHub.  

Do you want me to add that?
