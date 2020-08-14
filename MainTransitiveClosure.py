"""
	MainTransitiveClosure.py
	Calculates transitive closure using the Warshall algorithm
	and Fourth Theorem of Transitive Closure (Main)
	Author: Douglas De León, Isabel Ortiz, Pablo Ruiz
	Version: 1.0
	Date: Aug 14, 2020
"""

from TransitiveClosure import transitive_closure, warshall_algorithm

# Adjacency matrix for the relationship
R = [
    [0, 0, 1, 1],  # 1
    [1, 0, 0, 0],  # 2
    [0, 1, 0, 0],  # 3
    [0, 0, 0, 0],  # 4
]

# Program prints the transitive closure results of the relationship
print("*******************************************************************\n  Programa para hacer el cierre "
      "transitivo de matrices booleanas\n*******************************************************************")
print("Por: Douglas de León, Isabel Ortiz y Pablo Ruiz\n\n")
print("El resultado del cierre transitivo es el siguiente:")
transitive_closure(R)
print("\nPrograma que usa el algoritmo de Warshall para hacer el cierre transitivo de una relación")
warshall_algorithm(R)
print("\nGracias por usar el programa de cierre transitivo, que tenga un feliz día :)")
