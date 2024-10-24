import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

x = tf.constant(3, shape=(2,2))
print(x)

y = tf.constant([[34,6,7],[6,1,9]])
print(y)

z = tf.ones((2,3))
print(z)

s = tf.eye(3)
print(s)