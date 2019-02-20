

import tensorflow as tf


# Constant Node
constantNode1 = tf.constant(1.2, dtype=tf.float32)
constantNode2 = tf.constant(2.0)


# Operator Nodes
additionNode = tf.add(constantNode1, constantNode2)

print(additionNode)


# Placeholder Nodes
placeholder1 = tf.placeholder(dtype=tf.float32)

# Example
multiply = tf.multiply(constantNode2, placeholder1)

# Creating Session
session = tf.Session()
print(session.run(multiply, {placeholder1: 4.0}))
