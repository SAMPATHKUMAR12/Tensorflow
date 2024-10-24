import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

x = tf.constant([1,23,45])
y = tf.constant([6,1,8])

# z =x+y
z= tf.add(x,y)
print(z)

k = tf.subtract(x,y)
print(k)

m = tf.multiply(x,y)  #element wise multi
print(m)

s = tf.tensordot(x,y, axes=1)  #dot product
print(s)

n = tf.divide(x,y)
print(n)
