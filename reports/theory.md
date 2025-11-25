🧠 Perceptron Theory

A simple explanation of how a perceptron works, how it learns, and why it is the foundation of modern neural networks.

1. What Is a Perceptron?

A perceptron is the simplest type of artificial neural network.
It is a binary classifier — meaning it predicts either 0 or 1.

A perceptron:

Receives input values

Multiplies them by weights

Adds a bias

Applies an activation function

Produces 0 or 1

It is the building block for all deep learning architectures today.

2. Perceptron Architecture

A perceptron takes multiple inputs:

𝑥
1
,
𝑥
2
,
.
.
.
,
𝑥
𝑛
x
1
	​

,x
2
	​

,...,x
n
	​


and learns corresponding weights:

𝑤
1
,
𝑤
2
,
.
.
.
,
𝑤
𝑛
w
1
	​

,w
2
	​

,...,w
n
	​


Then computes a weighted sum:

𝑧
=
𝑤
1
𝑥
1
+
𝑤
2
𝑥
2
+
.
.
.
+
𝑤
𝑛
𝑥
𝑛
+
𝑏
z=w
1
	​

x
1
	​

+w
2
	​

x
2
	​

+...+w
n
	​

x
n
	​

+b

where b is the bias.

3. Activation Function (Step Function)

After computing the weighted sum, the perceptron passes it through a very simple activation:

𝑜
𝑢
𝑡
𝑝
𝑢
𝑡
=
{
1
	
if 
𝑧
≥
0


0
	
if 
𝑧
<
0
output={
1
0
	​

if z≥0
if z<0
	​


This is called the Heaviside step function.

It converts a continuous value into a binary output.

4. How the Perceptron Learns (Training Rule)

The perceptron updates weights using the Perceptron Learning Rule.

1️⃣ Compute prediction
𝑦
^
=
𝑎
𝑐
𝑡
𝑖
𝑣
𝑎
𝑡
𝑖
𝑜
𝑛
(
𝑤
⋅
𝑥
+
𝑏
)
y
^
	​

=activation(w⋅x+b)
2️⃣ Compute error
𝑒
𝑟
𝑟
𝑜
𝑟
=
𝑦
−
𝑦
^
error=y−
y
^
	​

3️⃣ Update weights and bias
𝑤
𝑖
=
𝑤
𝑖
+
𝑙
𝑟
⋅
𝑒
𝑟
𝑟
𝑜
𝑟
⋅
𝑥
𝑖
w
i
	​

=w
i
	​

+lr⋅error⋅x
i
	​

𝑏
=
𝑏
+
𝑙
𝑟
⋅
𝑒
𝑟
𝑟
𝑜
𝑟
b=b+lr⋅error

Where:

lr = learning rate

y = true label

ŷ = predicted label

Key idea:

If prediction is correct, error = 0 → no update

If prediction is wrong, the weights shift toward the correct direction

5. What Is Learning Rate (lr)?

lr controls how big each weight update is.

Too large: jumps too far → unstable learning

Too small: tiny updates → slow convergence

Typical values: 0.01 – 0.1.

6. Linearly Separable Problems

A perceptron can only solve problems where you can draw a straight line between classes.

Examples:

AND → separable

OR → separable

NAND → separable

But some problems are NOT linearly separable:

❌ XOR

You cannot separate XOR outputs with a single straight line.
This is why XOR requires multi-layer networks (MLP).

7. Logic Gate Examples
AND Gate
x1	x2	y
0	0	0
0	1	0
1	0	0
1	1	1
OR Gate
x1	x2	y
0	0	0
0	1	1
1	0	1
1	1	1
NAND Gate
x1	x2	y
0	0	1
0	1	1
1	0	1
1	1	0

These functions are all learnable by a perceptron.

8. Training Workflow (Step-by-Step)
1️⃣ Initialize model

Random weights

Random bias

2️⃣ For each epoch:

Repeat for all samples in the dataset:

Compute weighted sum

Apply activation

Compute error

Update weights & bias

3️⃣ After enough epochs

The model converges and learns the correct decision boundary.

4️⃣ Test

Use the trained perceptron to make predictions.

9. Limitations of a Single Perceptron

A single-layer perceptron:

❌ Cannot learn XOR

❌ Cannot create non-linear boundaries

❌ Only works for binary outputs

❌ Uses a very simple activation (step function)

These limitations led to the development of:

Multi-Layer Perceptrons (MLP)

Backpropagation

Deep Learning

10. Summary

A perceptron is the simplest neural network unit.

It performs a weighted sum and passes it through a step function.

It learns using the perceptron update rule.

It can learn AND, OR, NAND, and other linearly separable functions.

It cannot learn XOR or any non-linear patterns.

It is the foundation of modern deep learning systems.