import random

class Cartas:

	def __init__(self,valor,naipe):

		self.valor = valor
		self.naipe = naipe

	def show(self):

		print("{} de {}".format(self.valor, self.naipe))

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

	def __init__(self, nome):

		self.nome = nome
		self.mao = []

	def compra_carta(self, deck):

		self.mao.append(deck.compra())

		return self

	def mostra_mao(self):

		for carta in self.mao:
			carta.show()







deck = Deck()
deck.build()
deck.show()
deck.shuffle()
deck.show()

Jogador1 = Jogador("Felippe")
print(Jogador1.nome)
Jogador1.compra_carta(deck).compra_carta(deck)
Jogador1.mostra_mao()


#carta = deck.compra()
#carta.show()


