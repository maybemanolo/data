class Operation():

	def __init__(self,input_nodes=[]):
		self.input_nodes = input_nodes
		self.output_nodes = []

		for node in input_nodes:
			node.output_nodes.append(self)

		_default_graph.operations.append(self)

	def compute(self):
		pass

class add(Operation):

	def __init__(self,x,y):
		super().__init__([x,y])

	def compute(self,x_var,y_var):
		self.inputs = [x_var,y_var]
		return x_var + y_var

class multiply(Operation):

	def __init__(self,x,y):
		super().__init__([x,y])

	def compute(self,x_var,y_var):
		self.inputs = [x_var,y_var]
		return x_var * y_var

class matmul(Operation):

	def __init__(self,x,y):
		super().__init__([x,y])

	def compute(self,x_var,y_var):
		self.inputs = [x_var,y_var]
		return x_var.dot(y_var)

class Placeholder():

	def __init__(self):
		self.output_nodes = []

		_default_graph.placeholder.append(self)

class Variable():

	def __init__(self,initial_value=None):
		self.value = initial_value
		self.output_nodes = []

		_default_graph.variable.append(self)

class Graph():

	def __init__(self):
		self.operations = []
		self.placeholders = []
		self.variables = []

	def set_as_default(self):
		global _default_graph
		_default_graph = self

g = Graph()
g.set_as_default()
A = Variable(10)
b = Variable(1)
x = Placeholder()
y = multiply(A,x)
z = add(y,b)

def traverse_postorder(operation):
	nodes_postorder = []

	def recurse(node):
		if isinstance(node, Operation):
			for input_node in node.input_nodes:
				recurse(input_node)
			nodes.postorder.append(node)
	recurse(operation)

	return nodes_postorder

class Session():

	def run(self,operation,feed_dict={}):
		nodes_postorder = traverse_postorder(operation)
		for node in nodes_postorder:
			if type(node) == Placeholder:
				node.output = feed_dict[node]
			elif type(node) == Variable:
				node.output = node.value
			else:
				node.inputs = [input_node.output for input_node in node.input_nodes]
				node.output = node.compute(*node.inputs)
			if type(node.output) == list:
				node.output = np.array(node.output)
		return operation.output

sess = Session()
result = sess.run(operation=z,feed_dict={x:10})

g2 = Graph()
g2.set_as_default()
A2 = Variable([[10,20],[30,40]])
B2 = Vairable([1,2])
x2 = Placeholder()
y2 = matmul(A2,x2)
z2 = add(y2,B2)

sess2 = Session()
sess.run(operation=z,feed_dict={x:10})