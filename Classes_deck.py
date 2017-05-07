import random

class Cartas:

	def __init__(self,valor,naipe):

		self.valor = valor
		self.naipe = naipe

	def show(self):
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


class Deck:

	def __init__(self):

		self.cartas = []
		self.build()

	def build(self):

		for i in ["Ouros","Paus","Copas","Espadas"]:

			for c in range(1,14):

				self.cartas.append(Cartas(c,i))

	def show(self):

		for x in self.cartas:

			x.show()

	def shuffle(self):

		for i in range(len(self.cartas)-1,0,-1):
			
			r = random.randint(0,i)

			self.cartas[i], self.cartas[r] = self.cartas[r], self.cartas[i]

	def compra(self):

		return self.cartas.pop()

class Jogador:

	def __init__(self, nome,fichas):

		self.nome = nome
		self.mao = []
		self.fichas = fichas
		lista_jogadores.append(self)

	def compra_carta(self, deck):

		self.mao.append(deck.compra())

		return self

	def mostra_mao(self):

		for carta in self.mao:
			carta.show()

	def acao(self,deck):
		if maior_aposta == 0: 
			acao=input("Check(C), Raise(R), Fold(F)").lower()
			if acao == "check" or acao == "c":
				print("{} checa!".format(self))
			if acao == "raise" or acao == "r":
				aposta=int(input("Quanto deseja apostar?"))
				self.fichas -=aposta
				print("{} aposta {} fichas!".format(self,aposta))
				if aposta > maior_aposta:
					maior_aposta = aposta
				pot+=aposta
			if acao == "fold" or acao == "f":
				lista_jogadores.remove(self)
				print("{} sai da rodada!".format(self))

		if maior_aposta > 0:
			acao=input("Call(C), Raise(R), Fold(F)").lower()
			if acao == "call" or acao == "c":
				print("{} paga pra ver!".format(self))
				self.fichas -= maior_aposta
				pot+=aposta
			if acao == "raise" or acao == "r":
				aposta=int(input("Quanto deseja apostar?"))
				self.fichas -=aposta
				print("{} aposta {} fichas!".format(self,aposta))
				if aposta > maior_aposta:
					maior_aposta = aposta
				pot+=aposta
			if acao == "fold" or acao == "f":
				lista_jogadores.remove(self)
				print("{} sai da rodada!".format(self))


class Rodada:

	def __init__(self,lista_jogadores):
		lista_jogadores=[]
		pot=0
		deck = Deck()
		deck.shuffle()
		for i in lista_jogadores:
			i.compra_carta(deck).compra_carta(deck)
			i.mostra_mao()

	def flop(self,deck):
		maior_aposta=0
		mesa=[]
		mesa.append(deck.compra())
		mesa.append(deck.compra())
		mesa.append(deck.compra())
		print(mesa[0]+ " - " + mesa[1] + " - " + mesa[2])
		for i in lista_jogadores:
			i.acao(deck)
	
	def turn(self,deck):
		maior_aposta=0
		mesa.append(deck.compra())
		print(mesa[0] + " - " + mesa[1] + " - " + mesa[2] + " - " + mesa[3])
		for i in lista_jogadores:
			i.acao(deck)
	
	def river(self,deck):
		maior_aposta=0
		mesa.append(deck.compra())
		print(mesa[0] + " - " + mesa[1] + " - " + mesa[2] + " - " + mesa[3] + " - " + mesa[4])
		for i in lista_jogadores:
			i.acao(deck)




