import os
import tensorflow as tf

def loadword2vecpath():
	word2vec = tf.load_op_library(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'word2vec_ops.cc'))

	return word2vec