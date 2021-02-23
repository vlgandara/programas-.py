# Aluno: Vinícius Lopes Gandara  Matrícula: 134.507
# 
# Implementação de uma Pilha em Python3  Programa: pilha.py

class Menu:
	def __init__(self):
		self.pilha = []
		self.opcoes = {     # Menu relacioando opções com métodos
				"U": self.push,
				"O": self.pop,
				"E": self.peek
				}

	def menu(self):
		while True:
			opcao = input("Digite a operação desejada (U para PUSH, O para POP ou E para PEEK):")
			executar = self.opcoes.get(opcao.upper()) # Pega a opção digitada pelo usuário e transforma em maiúscula e executa o método relacionado com a opção digitada.
			if executar:
        			executar()

	def push(self):    # Método PUSH -> Adiciona um valor na pilha.
		valor = input("Entre com o valor: ")
		self.pilha.append(valor)

	def pop(self):   # Método POP -> Retira o último valor adicionado na pilha.
		if (self.pilha == []):  # Se a Pilha estiver Vazia.
			print("Pilha vazia")
		else:
			indice = len(self.pilha) - 1 # indice para identificar a útima posição da pilha.
			ultimo = self.pilha[indice]  # Seleção do elemento presente na última posição da pilha.
			self.pilha.remove(ultimo)  # Função POP.
			print("Retirou: ", ultimo) 

	def peek(self):   # Método PEEK -> Mostra o elemento do topo da pilha.
		if (self.pilha == []): # Se a pilha estiver Vazia.
			print("Pilha vazia")
		else:
			indice = len(self.pilha) - 1  # indice para identificar a útima posição da pilha.
			ultimo = self.pilha[indice]  # Seleção do elemento presente na última posição da pilha.
			print("Último elemento da pilha: ", ultimo)

if __name__ == "__main__":  # Executa em primeiro plano o Menu quando inicado o programa.
	Menu().menu()
