import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

x = tf.constant(3, shape=(2,2))
print(x) 

# print(tf.zeros(3))