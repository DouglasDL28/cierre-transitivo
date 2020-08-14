"""
	MainTranstiveClosure.py
	Calculates transitive closure using the Warshall algorithm
	and Fourth Theorem of Transitive Closure (Main)
	Author: Douglas De León, Isabel Ortiz, Pablo Ruiz
	Version: 1.0
	Date: Aug 14, 2020
"""

from TransitiveClosure import transitive_closure,warshall_algorithm

# Se define la matriz de adyacencia del grafo 
R = [
	[0, 0, 1, 1],		# 1
	[1, 0, 0, 0],		# 2
	[0, 1, 0, 0],		# 3
	[0, 0, 0, 0],		# 4
]

print("     Programa para hacer el cierre transitivo de matrices booleanas \n")
print("     El resultado del cierre transitivo es el siguiente: \n")
transitive_closure(R)
print(      "Programa que usa el algoritmo de Warshall para hacer el cierre transitivo de una relacion \n")
warshall_algorithm(R)

