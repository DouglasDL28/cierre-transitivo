"""
	TransitiveClosure.py
	Calculates transitive closure using the Warshall algorithm
	and Fourth Theorem of Transitive Closure
	Author: Douglas De León, Isabel Ortiz, Pablo Ruiz
	Version: 1.0
	Date: Aug 14, 2020
"""
import numpy as np


# todo: Poner esto en el main
R = [
	[0, 0, 1, 1],		# 1
	[1, 0, 0, 0],		# 2
	[0, 1, 0, 0],		# 3
	[0, 0, 0, 0],		# 4
]


def transitive_closure(matrix):
	"""
	Calculates the transitive closure of a relationship based on the fourth theorem
	of transitive closure: MR^* = MR V MR^2 V ... V MR^n
	:param matrix: Boolean matrix of the relationship R (list of lists)
	"""
	# Original matrix, power matrix, and result matrix
	matrix = np.array(matrix, dtype=bool)
	power_matrix = matrix
	result = matrix

	# Prints the adjacency matrix
	print("\nMATRIZ DE ADYACENCIA")
	for row in 1 * matrix:
		print(row)

	# Calculates the power matrices and performs the or
	for i in range(2, len(matrix) + 1):
		power_matrix = np.matmul(power_matrix, matrix)
		result = np.bitwise_or(result, power_matrix)

	# Prints the transitive closure matrix
	print("\nMATRIZ RESULTANTE (Cierre transitivo por Teorema 4)")
	for row in 1 * result:
		print(row)


def warshall_algorithm(matrix):
	"""
	Calculates transitive closure using the Warshall algorithm
	:param matrix: Boolean matrix of the relationship R (list of lists)
	"""
	# Prints the adjacency matrix
	print("\nMATRIZ DE ADYACENCIA")
	for row in matrix:
		print(row)

	# Warshall algorithm
	for k in range(0, len(matrix)):
		for i in range(0, len(matrix)):
			for j in range(0, len(matrix)):
				matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

	# Prints the transitive closure matrix
	print("\nMATRIZ RESULTANTE (Cierre transitivo por Warshall)")
	for row in matrix:
		print(row)


# todo: Eliminar esto cuando se tenga implementado el main
transitive_closure(R)
warshall_algorithm(R)

