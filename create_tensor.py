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

k = tf.random.uniform((1,3), minval=0, maxval=1)
print(k)

m =tf.range(10, delta=2)
print(m)

x= tf.cast(x, dtype=tf.float64)
print(x)