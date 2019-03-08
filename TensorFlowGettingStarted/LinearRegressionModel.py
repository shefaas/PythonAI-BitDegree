

import tensorflow as tf

# Linear Regression formula: y = W*x + b
# W refers to Weight while it is the same as we previously saying m

# For training step:
#      - x and y will be placeholder nodes since they will be given data to guide the model.
#      - W and b will be variable nodes since we will initiate them then the model will optimize their values.


# For testing step:
#     - x will be placeholder.
#     - y will be variable. It will be predicted.
#     - W and b will be variable nodes.


# Training Data:
# x = [ 1, 2, 3, 4]
# y = [ 0, -1, -2, -3]

W = tf.Variable([-.5], dtype=tf.float32)
b = tf.Variable([.5], dtype=tf.float32)

# Creating placeholders for x and y
x = tf.placeholder(dtype=tf.float32)
y = tf.placeholder(dtype=tf.float32)


# Preparing the values that will be given for x and y
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]


# Linear regression formula
linear_model = (W * x) + b

# Loss function (to get the accuracy)
loss = tf.reduce_sum(tf.square(linear_model - y_train))

# Optimizing W and b values
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Creating a session
session = tf.Session()
initializer = tf.global_variables_initializer()
session.run(initializer)

# print(session.run(linear_model, {x: x_train}))
for i in range(1000):
    session.run(train, {x: x_train, y: y_train})

# Test instance
print(session.run(linear_model, {x: 3}))
