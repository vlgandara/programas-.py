# Aluno: Vinícius Lopes Gandara  Matrícula: 134.507
# 
# Implementação de uma Árvore Binária em Python3  Programa: ARVOREPYTHON3.py

class No:
	def __init__(self, n =' ', i=0):
		self.nome=n
		self.indice=i
		self.noE = None
		self.noD = None
		
		self.opcoes = {     # Menu relacionando opções com métodos
				"1": self.inserir,
				"2": self.remover,
				"3": self.listar_em_ordem,
				"4": self.pesquisar
				}

	def menu(self):
		while True:
			opcao = input("Digite a operação desejada (1 para INSERIR, 2 para REMOVER, 3 para LISTAR EM ORDEM 4 para PESQUISAR):")
			executar = self.opcoes.get(opcao) # Pega a opção digitada pelo usuário e executa o método relacionado com a opção digitada.
			if executar:
        			executar()

	def inserir(self, no):
		if no.nome > self.nome:
			if self.noD:
				self.noD.inserir(no)
			else:
				self.noD= no
		else:
			if self.noE:
				self.noE.inserir(no)
			else:
				self.noE= no
	def remover(self):
		print("a")
	
	def listar_em_ordem(self):
		if self.noE:
			self.noE.listar_em_ordem()
			print(self.nome)
		if self.noD:
			self.listar_em_ordem()

	def pesquisar(self, nomeB):
		nomeB = nomeB.upper()
		if self.nome == nomeB:
		       	return self
		if self.nome > nomeB:
			if not self.noE: return None
			return self.noE.pesquisar(nomeB)
		else:
			if not self.noD: return None
			return self.noD.pesquisar(nomeB)


inf = open("C:\ed2019\cadastro2019.csv",encoding='l2')

li = inf.readline()
fpos = inf.tell()
li = inf.readline()

arvore = None

while(li):
	
	novoNo = No( str(li).split('|')[2],fpos )
	if not arvore:
		arvore = novoNo
		inicio=False
	else:
		arvore.inserir(novoNo)
	
	fpos = inf.tell()
	li = inf.readline()

				
if __name__ == "__main__":
	No().menu()
		
		

