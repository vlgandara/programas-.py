minha_matriz = [[1, 2], [3, 4], [5,6]]

def imprime_matriz(minha_matriz):
	
	lin = len(minha_matriz)
	col = len(minha_matriz[0])

	for i in range(lin):
		for j in range(col):
			if (j != (col-1)) :
				print(minha_matriz[i][j],end=' ')
			else : 
				print(minha_matriz[i][j])

imprime_matriz(minha_matriz)