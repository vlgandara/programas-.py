# Aluno: Vinícius Lopes Gandara  Matrícula: 134.507
# 
# Implementação de uma Árvore Binária em Python3  Programa: ARVOREPYTHON3.py

class Menu:
	def __init__(self):
		self.item_menor = None
		self.item_maior = None
		self.opcoes = {     # Menu relacionando opções com métodos
				"1": self.inserir,
				"2": self.remover,
				"3": self.listar_em_ordem,
				"4": self.pesquisar
				}

	def menu(self):
		self.indexaCadastro
		while True:
			opcao = input("Digite a operação desejada (1 para INSERIR, 2 para REMOVER, 3 para LISTAR EM ORDEM 4 para PESQUISAR):")
			executar = self.opcoes.get(opcao) # Pega a opção digitada pelo usuário e executa o método relacionado com a opção digitada.
			if executar:
        			executar()
	
	def indexaCadastro(nomeArquivo, nomeIndice):

		arq = open("C:\ed2019\cadastro2019.csv",encoding='l2')
		ndx = open("C:\ed2019\arqind.txt","w")

		fpos = arq.tell()
		linha = arq.readline()
		while(linha):
			ndx.write(str(fpos)+","+str(linha).split('|')[2]+"\n") # Posição e nome
			fpos = arq.tell()
			linha = arq.readline()


	def inserir(self):
		self.nome = nome
		self.indice = indice
		self.raiz = None
		self.lista_lado_menor = []
		self.lista_lado_maior = []
		i = 0
		j = 0
		if (raiz == None):  # 1ª Situação: 1º elemento da Árvore Binária. Não existe raiz
			self.nome = raiz
		elif(self.nome < raiz) and (self.item_menor == None): # 2ª Situação: 1º elemento a ser adicionado ao lado esquerdo da Árvore Binária
			self.nome = self.item_menor(i)
			self.lista_lado_menor.append(self.nome) 
		elif(self.nome > raiz) and (self.item_maior == None): # 3ª Situação: 1º elemento a ser adicionado ao lado direito da Árvore Binária
			self.nome = self.item_maior(j)
			self.lista_lado_maior.append(self.nome)
		elif(raiz != None):
			if(self.nome < self.item_menor(i)):  # 4ª Situação: Elemento a ser adicionado ao lado esquerdo do 1º elemento menor que a raiz
				--i
				self.nome = item_menor(i)
				self.lista_lado_menor.append(self.nome)
			elif(self.nome > self.item_menor(i)): # 5ª Situação: Elemento a ser adicionado ao lado direito do 1º elemento menor que a raiz
				--i
				self.nome = item_menor(i * -1)
				self.lista_lado_menor.append(self.nome)
			elif(self.nome < self.item_maior(j)): # 6ª Situação: Elemento a ser adicionado ao lado esquerdo do 1º elemento maior que a raiz
				--j
				self.nome = item_maior(j)
				self.lista_lado_maior.append(self.nome)
			elif(self.nome > self.item_maior(j)): # 7ª Situação: Elemento a ser adicionado ao lado direito do 1º elemento maior que a raiz
				--j				
				self.nome = item_maior(j * -1)
				self.lista_lado_maior.append(self.nome)
	
	def remover(self):
		removido = input("Digite o nome do funcionário que deseja remover da árvore binária: ")
		if (self.removido in self.lista_lado_menor): # Remove o funcionário escolhido pelo usuário caso esteja no lado esquerdo da raiz
			self.lista_lado_menor.remove(removido)
			print("Usuário removido!")
		elif (self.removido == self.raiz): # Remove o funcionário escolhido pelo usuário caso esteja na raiz
			self.raiz.remove(removido)
			print("Usuário removido!")
		elif (self.removido in self.lista_lado_maior): # Remove o funcionário escolhido pelo usuário caso esteja no lado direito da raiz
			self.lista_lado_maior.remove(removido)
			print("Usuário removido!")
		else:  # Funcionário escolhido pelo usuário não encontrado
			print("Funcionário não encontrado!") 
			

	def listar_em_ordem(self):   # Ordena em ordem alfabética os funcionários da Árvore Binária
		self.lista_lado_menor.sort()
		self.lista_lado_maior.sort()
		print(self.lista_lado_menor, self.raiz, self.lista_lado_maior)

	def pesquisar(self):
		self.procurado = input("Digite o nome do funcionário que deseja pesquisar: ")
		if (self.procurado in self.lista_lado_menor):  # Procura o funcionário escolhido pelo usuário caso esteja no lado esquerdo da raiz
			print(self.procurado)
		elif (self.procurado == self.raiz): # Procura o funcionário escolhido pelo usuário caso esteja na raiz
			print(self.procurado)
		elif (self.procurado in self.lista_lado_maior): # Procura o funcionário escolhido pelo usuário caso esteja no lado direito da raiz
			print(self.procurado)
		else:  # Funcionário escolhido pelo usuário não encontrado
			print("Funcionário não encontrado!")

	def carregaIndice(self, nomeIndice):
		arq = open(nomeIndice)
		linha = arq.readline()
		while(linha):
			self.inserir(linha.split(',')[0],linha.split(',')[1] )
			linha = arq.readline()
				
if __name__ == "__main__":
	Menu().menu()
		
		

