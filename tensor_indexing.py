import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

x = tf.constant([1,2,3,45,6,67,8])

print(x[1:])

