'''
Author: Sam Helms
Date: Nov 1

This class creates an scatter plot for visualizing
embeddings (probably using TSNE)

'''

class Scatter:
	def __init__(self, data, ):
		if type(data) == "str":
			print "creating table from path"
			# read the file and create indices
		else:
			# create indices and then write out 
			# to a file in a format the table can use
			None

