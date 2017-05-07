import random

class Cartas: # Cartas do baralho

	def __init__(self,valor,naipe): # Define valor e naipe da carta

		self.valor = valor
		self.naipe = naipe

	def show(self): # Altera as carta 1, 11, 12, 13 para Ás, J, Q, K, respectivamente

		if 1<self.valor<=10: 
			print("{} de {}".format(self.valor, self.naipe))
		if self.valor==1:
			print("{} de {}".format("A", self.naipe))
		if self.valor==11:
			print("{} de {}".format("J", self.naipe))
		if self.valor==12:
			print("{} de {}".format("Q", self.naipe))
		if self.valor==13:
			print("{} de {}".format("K", self.naipe))


class Deck: # Baralho

	def __init__(self): # Define o que é o baralho

		self.cartas = []
		self.build()

	def build(self): # Função que cria cada carta com seu naipe e valor

		for i in ["Ouros","Paus","Copas","Espadas"]:

			for c in range(1,14):

				self.cartas.append(Cartas(c,i))

	def show(self): # Função para mostrar as cartas do baralho

		for x in self.cartas:

			x.show()

	def shuffle(self): # Embaralha todas as cartas

		for i in range(len(self.cartas)-1,0,-1):
			
			r = random.randint(0,i)

			self.cartas[i], self.cartas[r] = self.cartas[r], self.cartas[i]

	def compra(self): # Adiquire uma carta

		return self.cartas.pop()

class Jogador: # Jogador

	def __init__(self, nome,fichas): # Define o nome do jogador, suas cartas e a quantidade de fichas disponíveis

		self.nome = nome
		self.mao = []
		self.fichas = fichas
		lista_jogadores.append(self)

	def compra_carta(self, deck): # Atualiza a mão do jogador através da função de comprar cartas da classe baralho

		self.mao.append(deck.compra())

		return self

	def mostra_mao(self): # Mostra as cartas que estão na mão do jogador

		for carta in self.mao:
			carta.show()

	def acao(self,deck): # Possibilidade de dar call, fold, apostar ou check

		if maior_aposta == 0: # Caso não exista uma aposta
			acao=input("Check(C), Raise(R), Fold(F)").lower()

			if acao == "check" or acao == "c": # Check: continua a rodada sem apostar
				print("{} checa!".format(self))

			if acao == "raise" or acao == "r": # Aposta: coloca uma aposta na mesa
				aposta=int(input("Quanto deseja apostar?"))
				self.fichas -=aposta
				print("{} aposta {} fichas!".format(self,aposta))

				if aposta > maior_aposta:
					maior_aposta = aposta
				pot+=aposta

			if acao == "fold" or acao == "f": # Fold: desiste da mão
				lista_jogadores.remove(self)
				print("{} saiu da rodada!".format(self))

		if maior_aposta > 0: # Caso exista uma aposta na mesa
			acao=input("Call(C), Raise(R), Fold(F)").lower()

			if acao == "call" or acao == "c": # Call: iguala a aposta da mesa
				print("{} paga pra ver!".format(self))
				self.fichas -= maior_aposta
				pot+=aposta

			if acao == "raise" or acao == "r": # Aumenta a aposta
				aposta=int(input("Quanto deseja apostar?"))
				self.fichas -=aposta
				print("{} aposta {} fichas!".format(self,aposta))

				if aposta > maior_aposta:
					maior_aposta = aposta
				pot+=aposta

			if acao == "fold" or acao == "f": # Fold: desiste da rodada
				lista_jogadores.remove(self)
				print("{} sai da rodada!".format(self))


class Rodada: # Rodada

	def __init__(self,lista_jogadores): 
		lista_jogadores=[] # Atualiza os jogadores da rodada
		pot=0 # Atualiza a soma das apostas na Rodada
		deck = Deck() # Reestaura o baralho
		deck.shuffle() # Emabaralha o deck
		for i in lista_jogadores: # Define as mãos dos jogadores participantes
			i.compra_carta(deck).compra_carta(deck)
			i.mostra_mao()

	def flop(self,deck): # Vira as 3 primeiras cartas
		maior_aposta=0 
		mesa=[] # Esvazia a mesa da rodada anterior
		mesa.append(deck.compra()) # Abre uma carta na mesa
		mesa.append(deck.compra()) # Abre uma carta na mesa
		mesa.append(deck.compra()) # Abre uma carta na mesa
		print(mesa[0]+ " - " + mesa[1] + " - " + mesa[2]) # Mostra as cartas abertas
		for i in lista_jogadores: # Confere a ação de cada jogador na rodada
			i.acao(deck)
	
	def turn(self,deck):
		maior_aposta=0
		mesa.append(deck.compra()) # Abre uma carta na mesa
		print(mesa[0] + " - " + mesa[1] + " - " + mesa[2] + " - " + mesa[3]) # Mostra as cartas abertas
		for i in lista_jogadores: # Confere a ação de cada jogador na rodada
			i.acao(deck)
	
	def river(self,deck):
		maior_aposta=0
		mesa.append(deck.compra()) # Abre uma carta na mesa
		print(mesa[0] + " - " + mesa[1] + " - " + mesa[2] + " - " + mesa[3] + " - " + mesa[4]) # Mostra as cartas abertas
		for i in lista_jogadores: # Confere a ação de cada jogador na rodada
			i.acao(deck)




