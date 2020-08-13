import numpy as np

R = [
	[0,0,1,1], #1
	[1,0,0,0], #2
	[0,1,0,0], #3
	[0,0,0,0], #4
]

print("MATRIZ DE ADYACENCIA")
for row in range(0, len(R)):
	print(R[row])

print("\nCantidad de vértices: ", len(R))

# Algoritmo de Warshall
for k in range(0, len(R)):
	for i in range(0, len(R)):
		for j in range(0, len(R)):
			R[i][j] = R[i][j] or (R[i][k] and R[k][j])


print("\nMATRIZ RESULTANTE (Cierre transitivo)")
for row in range(0, len(R)):
	print(R[row])

