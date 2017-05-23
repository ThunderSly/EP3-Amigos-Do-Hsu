import itertools
import random
import time
import pickle

class Cartas: # Cartas do baralho

	def __init__(self, valor, naipe, sprite): # Define valor e naipe da carta

		self.valor = valor
		self.naipe = naipe
		self.sprite = sprite
		#self.sprite = sprite

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
		naipes=["Ouros","Paus","Copas","Espadas"]
		
		
		for i in naipes:

			for c in range(1, 14):

				z = "Sprites\\{} de {}.png" .format(c,i)

				self.cartas.append(Cartas(c,i,z))
				

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

	def __init__(self,nome,fichas): # Define o nome do jogador, suas cartas e a quantidade de fichas disponíveis

		self.nome = nome
		self.mao = []
		self.fichas = fichas
		self.maior_aposta=0
		lista_jogadores.append(self)

	def compra_carta(self, deck): # Atualiza a mão do jogador através da função de comprar cartas da classe baralho

		self.mao.append(deck.compra())

		return self.mao

	def reseta_mao(self):

		self.mao = []

		return self

	def mostra_mao(self): # Mostra as cartas que estão na mão do jogador

		print("Sua mão:")
		for carta in self.mao:
			carta.show()

	def acao(self,deck): # Possibilidade de dar call, fold, apostar ou check
		maior_aposta = 0
		pot = 0
		while True:
			if maiores_apostas.count(max(maiores_apostas)) == len(lista_jogadores):
				break
			if maior_aposta == 0:
				acao=input("Check(C), Raise(R), Fold(F)\n").lower()
				if acao == "check" or acao == "c": # Check: continua a rodada sem apostar

					print("{} checa!".format(self.nome))
					maiores_apostas.append(0)

					break

				if acao == "raise" or acao == "r": # Aposta: coloca uma aposta na mesa
					aposta=int(input("Quanto deseja apostar?\n"))
					if aposta<self.fichas:
						self.fichas -=aposta

						print("{} aposta {} fichas!".format(self.nome,aposta))
						maior_aposta = aposta
						maiores_apostas.append(aposta)

						pot+=aposta
						self.maior_aposta=aposta
						break


					if aposta == self.fichas:
						self.fichas -= self.fichas
						print("{} ESTA ALL IN!".format(self.nome))
						maior_aposta = aposta
						maiores_apostas.append(aposta)

						pot+=aposta
						break
					if aposta > self.fichas:
						print("Você não tem essa quantidade de fichas!")
						continue

				if acao == "fold" or acao == "f": # Fold: desiste da mão
					lista_jogadores.remove(self)
					print("{} saiu da rodada!".format(self))
					break
			if maior_aposta > 0:
				acao=input("Call(C), Raise(R), Fold(F)\n").lower()

				if acao == "call" or acao == "c": # Call: iguala a aposta da mesa
					
					if maior_aposta<self.fichas:

						self.fichas -=(maior_aposta-self.maior_aposta)
						print("{} paga pra ver!".format(self.nome))
						maiores_apostas.append(maior_aposta)

						pot+=maior_aposta
					
					if maior_aposta >= self.fichas:
						pot+=self.fichas
						self.fichas == 0

						print("{} ESTA ALL IN!".format(self.nome))
						maiores_apostas.append(maior_aposta)

					break

				if acao == "raise" or acao == "r": # Aposta: coloca uma aposta na mesa
					aposta=int(input("Quanto deseja apostar?\n"))


					if aposta<self.fichas and aposta>maior_aposta:
						self.fichas -=aposta
						print("{} aposta {} fichas!".format(self.nome,aposta))
						maior_aposta = aposta
						self.maior_aposta=aposta
						maiores_apostas.append(aposta)

						pot+=aposta
						break
					
					if aposta == self.fichas:
						self.fichas == 0
						print("{} ESTA ALL IN!".format(self))
						if aposta > maior_aposta:
							maior_aposta = aposta
						maiores_apostas.append(aposta)
						pot+=aposta
						break

					if aposta > self.fichas:
						print("Você não tem essa quantidade de fichas!")
						continue
				
				if acao == "fold" or acao == "f": # Fold: desiste da rodada
					lista_jogadores.remove(self)
					self.mao = []
					print("{} sai da rodada!".format(self))
					break

		valores=[maior_aposta,pot]
		return valores
		

	def melhor_mao(self,mesa):	
		
		cartas_jogadores=[]
		mesa=rodada.mesa
		cartas_jogadores = mesa + self.mao
		lista_valores = []
		lista_naipes = []
		combinacoes = []
		valor_mao = 0

		for i in cartas_jogadores:
			lista_valores.append(i.valor)
			lista_naipes.append(i.naipe)
			if i.valor == 1:
				lista_valores.remove(i.valor)
				lista_valores.append(14) 
			
		for i in lista_valores: #para definir pares,trincas e quadras
							
			if lista_valores.count(i) == 4: # Quadra
				for x in range(2):
					combinacoes.append(i)
							
			elif lista_valores.count(i) == 3:
				combinacoes.append(i)

			elif lista_valores.count(i) == 2:
				combinacoes.append(i)

		combinacoes.sort()
		if len(combinacoes) == 6:
			if combinacoes[0] == combinacoes[1] and combinacoes[2] == combinacoes[3] and combinacoes[4] == combinacoes[5]: #retirar o terceiro par
				if combinacoes[0] != combinacoes[2]:
					del combinacoes[0]
					del combinacoes[0]

		if len(combinacoes) == 7:
			maior = []
			for i in lista_valores:
				if lista_valores.count(i) == 2:
					maior.append(i)
			maior.sort()
			combinacoes.remove(maior[0])
			combinacoes.remove(maior[0])

		if len(combinacoes) == 2: # Par
			print("Par de {}".format(combinacoes[0]))
			valor_mao = 2			
			
		if len(combinacoes) == 4: # Dois Pares
			print("Dois pares de {} e de {}".format(combinacoes[0] , combinacoes[2]))
			valor_mao = 3
			
		if len(combinacoes) == 3: # Trinca
			print("Trinca de {}".format(combinacoes[0]))
			valor_mao = 4

		for i in cartas_jogadores:
			if i.valor == 14:
				lista_valores.append(1)
				lista_naipes.append(i.naipe)		
		
		for n in range(1, 11):				
			if n in lista_valores: #Straight
				if n+1 in lista_valores:
					if n+2 in lista_valores:
						if n+3 in lista_valores:
							if n+4 in lista_valores:
								print("Straight de {} a {}".format(n,n+4))
								valor_mao = 5

		for i in cartas_jogadores:
			if i.valor == 14:
				lista_valores.remove(1)
				lista_naipes.remove(i.naipe)

		for i in lista_naipes: 
			if lista_naipes.count(i) >= 5: #Flush
				print("Flush de {}".format(i))
				valor_mao = 6
			
		if len(combinacoes) == 5 or len(combinacoes) == 6: # Full House
			print("Full House")
			valor_mao = 7
			
		if len(combinacoes) >= 7: #Quadra
			valor_mao = 8

		for i in cartas_jogadores:
			if i.valor == 14:
				lista_valores.append(1)
				lista_naipes.append(i.naipe)
		
		"""for n in range(1,11): # Straight Flush				
			for c in ["Ouros","Paus","Copas","Espadas"]:
				for i in cartas_jogadores:
					if i.valor == n and i.naipe == c:
						if n + 1 in lista_valores and  in lista_naipes:
							if i.n + 2 in lista_valores and i.c in lista_naipes:
								if i.n + 3 in lista_valores and i.c in lista_naipes:
									if i.n + 4 in lista_valores and i.c in lista_naipes:
										valor_mao = 9
										if i.n == 10: #Royal Straight Flush
											valor_mao = 10"""
		
		for i in cartas_jogadores:
			if i.valor == 14:
				lista_valores.remove(i.valor)
				lista_naipes.remove(i.naipe)

		print(valor_mao)
		self.reseta_mao()
		return valor_mao
		
	def maos_iguais(self, valor_mao):

		valor_especifico = 0
		
		if valor_mao == 0: #pega a melhor carta
			valor_especifico=max(lista_valores)

		elif valor_mao == 2: #pega o valor do par
			for i in lista_valores:
				if lista_valores.count(i) == 2:
					valor_especifico = i

		elif valor_mao == 3: #pega o valor do maior par
			maior = []
			for i in lista_valores:
				if lista_valores.count(i) == 2:
					maior.append(i)
			valor_especifico = max(maior)

		elif valor_mao == 4: #pega o valor da trinca
			for i in lista_valores:
				if lista_valores.count(i) == 3:
					valor_especifico = i

		elif valor_mao == 5: #pega o valor do primeiro membro do Straight (final)
			for i in lista_valores:
				if i.valor == 14:
					lista_valores.append(1)
			for n in range(1, 11):
				if n in lista_valores:
					if n+1 in lista_valores:
						if n+2 in lista_valores:
							if n+3 in lista_valores:
								if n+4 in lista_valores:
									valor_especifico = n+4

		elif valor_mao == 6: #pega o valor do maior membro do Flush
			maior = []
			for x in lista_naipes:
				if lista_naipes.count(x) >= 5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor) 
					break
			valor_especifico = max(maior)

		elif valor_mao == 7: #pega o valor da trinca do Full House
			for i in lista_valores:
				if lista_valores.count(i) == 3:
					valor_especifico = i
					break

		elif valor_mao == 8: #pega o valor da quadra
			for i in lista_valores:
				if lista_valores.count(i) == 4:
					valor_especifico = i
					break

		elif valor_mao == 9: #pega o valor do Straight Flush (final)
			
			maior = []
			for x in lista_naipes:
				if lista_naipes.count(x) >= 5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			valor_especifico = max(maior)

		return valor_especifico

	def carta_a_carta_1(self, valor_mao):
		
		if valor_mao == 0: #pega o valor da segunda maior carta
			maior = []
			for x in lista_valores:
				maior.append(x)
			maior.sort(reverse = True)
			valor_especifico = maior[1]

		elif valor_mao == 2: #pega o valor da melhor carta fora o par
			maior = []
			for x in lista_valores:
				if lista_valores.count(x) != 2:	
					maior.append(x)
			valor_especifico = max(maior)

		elif valor_mao == 3: #pega o valor do menor par
			maior = []
			for x in lista_valores:
				if lista_valores.count(x) == 2:
					maior.append(x)
			valor_especifico = min(maior)

		elif valor_mao == 4: #pega o valor da maior carta fora a trinca
			maior = []
			for x in lista_valores:
				if lista_valores.count(x) != 3:
					maior.append(x)
			valor_especifico = max(maior)

		elif valor_mao == 6: #pega o valor da segunda maior carta do Flush
			maior = []
			for x in lista_naipes:
				if lista_naipes.count(x) >= 5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			maior.sort(reverse = True)
			valor_especifico = maior[1]

		elif valor_mao == 7: #pega o valor do par do Full House (final)
			maior = []
			for x in lista_valores:
				if lista_valores.count(x) == 2:
					maior.append(x)
			valor_especifico = max(maior)

		elif valor_mao == 8: #pega o valor da melhor carta fora a quadra (final)
			maior = []
			for x in lista_valores:
				if lista_valores.count(x) != 4:
					maior.append(x)
			valor_especifico = max(maior)

		return valor_especifico

	def carta_a_carta_2(self,valor_mao):


		if valor_mao==0: #pega o valor da terceira melhor carta
			maior=[]
			for x in lista_valores:
				maior.append(x)
			maior.sort(reverse=True)
			valor_especifico=maior[2]

		elif valor_mao==2: #pega o valor da segunda melhor carta fora o par
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)!=2:	
					maior.append(x)
			maior.sort(reverse=True)
			valor_especifico=maior[1]

		elif valor_mao==3: #pega a melhor carta fora os pares (final)
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)!=2:
					maior.append(x)
			valor_especifico=max(maior)

		elif valor_mao==4: #pega o valor da segunda melhor carta fora a trinca (final)
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)!=3:
					maior.append(x)
			maior.sort(reverse=True)
			valor_especifico=maior[1]

		elif valor_mao==6: #pega o valor da terceira melhor carta do Flush
			maior=[]
			for x in lista_naipes:
				if lista_naipes.count(x)>=5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			maior.sort(reverse=True)
			valor_especifico=maior[2]

		print(valor_especifico)
		return valor_especifico

	def carta_a_carta_3(self,valor_mao):

		if valor_mao==0: #pega o valor da quarta melhor carta
			maior=[]
			for x in lista_valores:
				maior.append(x)
			maior.sort(reverse=True)
			valor_especifico=maior[3]

		elif valor_mao==2: #pega o valor da terceira melhor carta fora o par (final)
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)!=2:	
					maior.append(x)
			maior.sort(reverse=True)
			valor_especifico=maior[2]

		elif valor_mao==6: #pega o valor da quarta melhor carta do Flush
			maior=[]
			for x in lista_naipes:
				if lista_naipes.count(x)>=5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			maior.sort(reverse=True)
			valor_especifico=maior[3]

	def carta_a_carta_4(self,valor_mao):

		if valor_mao==0: #pega o valor da quinta melhor carta (final)
			maior=[]
			for x in lista_valores:
				maior.append(x)
			maior.sort(reverse=True)
			valor_especifico=maior[4]

		elif valor_mao==6: #pega o valor da quinta melhor carta do Flush (final)
			maior=[]
			for x in lista_naipes:
				if lista_naipes.count(x)>=5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			maior.sort(reverse=True)
			valor_especifico=maior[4]

		return valor_especifico


class Bot:

	def __init__(self, nome, fichas):
		self.nome = nome
		self.mao = []
		self.fichas = fichas
		lista_jogadores.append(self)

	def compra_carta(self, deck): # Atualiza a mão do jogador através da função de comprar cartas da classe baralho

		self.mao.append(deck.compra())

		return self

	def reseta_mao(self):

		self.mao = []

		return self

	"""def pre_flop(self):
		if""" 



class Compara_Maos:


	def peneira(mesa, lista_jogadores):
		jogadores1=[]
		valor1=[]
		jogadores2=[]
		valor2=[]
		jogadores3=[]
		valor3=[]
		jogadores4=[]
		valor4=[]
		jogadores5=[]
		valor5=[]
		
		valor6=[]

		for i in lista_jogadores:
			x = Jogador.melhor_mao(i,mesa)
			valor1.append(x)
		maximo = max(valor1)

		if valor1.count(maximo) > 1:
			for u in valor1:
				if u == maximo:
					l = valor1.index(u)
					jogadores1.append(lista_jogadores[l])
			
			for i in jogadores1:
				x = Jogador.maos_iguais(i,maximo)
				valor2.append(x)
			maximo = max(valor2)
			
			if valor2.count(maximo) > 1:
				for u in valor2:
					if u == maximo:
						l = valor2.index(u)
						jogadores2.append(jogadores1[l])

				for i in jogadores2:
					x = Jogador.carta_a_carta_1(i,maximo)
					valor3.append(x)
				maximo = max(valor3)

				if valor3.count(maximo) > 1:
					for u in valor3:
						if u == maximo:
							l = valor3.index(u)
							jogadores3.append(jogadores2[l])
			
					for i in jogadores3:
						x = Jogador.carta_a_carta_2(i,maximo)
						valor4.append(x)
					maximo = max(valor4)

					if valor4.count(maximo) > 1:
						for u in valor4:
							if u == maximo:
								l = valor4.index(u)
								jogadores4.append(jogadores3[l])
			
						for i in jogadores4:
							x = Jogador.carta_a_carta_3(i,maximo)
							valor5.append(x)
						maximo = max(valor5)

						if valor5.count(maximo) > 1:
							for u in valor5:
								if u == maximo:
									l = valor5.index(u)
									jogadores5.append(jogadores4[l])
			
							for i in jogadores5:
								x = Jogador.carta_a_carta_4(i,maximo)
								valor6.append(x)
							maximo = max(valor6)

							ganhador = valor6.index(maximo)
							return jogadores5[ganhador]

						else:
							ganhador = valor5.index(maximo)
							return jogadores4[ganhador]

					else:
						ganhador = valor4.index(maximo)
						return jogadores3[ganhador]
				else:
					ganhador = valor3.index(maximo)
					return jogadores2[ganhador]

			else:
				ganhador = valor2.index(maximo)
				return jogadores1[ganhador]
		
		else:
			ganhador = valor1.index(maximo)
			return lista_jogadores[ganhador]

class Mesa: # Rodada

	def __init__(self, lista_jogadores, deck): 
		pot = 0 # Atualiza a soma das apostas na Rodada
		self.mesa=[]
		time.sleep(1)
		for i in lista_jogadores: # Define as mãos dos jogadores participantes
			i.compra_carta(deck)
			i.compra_carta(deck)
			return i.mao

	def flop(self, deck, mesa): # Vira as 3 primeiras cartas
		maior_aposta = 0 
		mesa.append(deck.compra()) # Abre uma carta na mesa
		mesa.append(deck.compra()) # Abre uma carta na mesa
		mesa.append(deck.compra()) # Abre uma carta na mesa
		print("Mesa")
		mesa[0].show(), mesa[1].show(), mesa[2].show() # Mostra as cartas abertas
		for i in lista_jogadores: # Confere a ação de cada jogador na rodada
			i.acao(deck)
		return mesa

	def turn(self, deck, mesa):
		maior_aposta = 0
		mesa.append(deck.compra()) # Abre uma carta na mesa
		print("Mesa")
		mesa[0].show(), mesa[1].show(), mesa[2].show(), mesa[3].show() # Mostra as cartas abertas
		for i in lista_jogadores: # Confere a ação de cada jogador na rodada
			i.acao(deck)
		return mesa
	
	def river(self, deck, mesa):
		maior_aposta = 0
		mesa.append(deck.compra()) # Abre uma carta na mesa
		print("Mesa")
		mesa[0].show(), mesa[1].show(), mesa[2].show(), mesa[3].show(), mesa[4].show() # Mostra as cartas abertas
		for i in lista_jogadores: # Confere a ação de cada jogador na rodada
			i.acao(deck)
		return mesa

class Jogo:	

	def inicio():
		print("Bem vindo ao Hsu Poker! ") # Começo do jogo
		x =Jogo.load()
		nome = x[0]
		fichas = x[1]
		time.sleep(1)
		return nome, fichas


	def fim():
		carregamento = Jogo.salvar()
		time.sleep(0.5)
		print("Até a próxima!") # Finalização do jogo # Inicio e fim do jogo

	def salvar():  # Função de salvar o jogo

		dados = open("jogo",'wb') 
		pickle.dump({"jogo" : [nome, fichas]}, dados)
		dados.close()
		time.sleep(0.5)
		print("Jogo salvo com sucesso!")

	def load():

		try: # Traz o jogo salvo com os dados guardados
			dado = pickle.load(open("jogo",'rb'))  
			nome = dado["jogo"][0]
			fichas = dado["jogo"][1]
			carregado = sim
			jogador = Jogador(nome, fichas)
			time.sleep(2)
			print("O nome do seu personagem é {}, você possui {} de fichas" .format(nome, fichas)) # Caracterização dos dados para o usuário

		except: # Cria um novo personagem
			dados = open("jogo",'wb')
			time.sleep(0.5)
			dados.close()
			nome = input("Qual vai ser o nome do seu personagem?\n")
			fichas = 10000
			jogador= Jogador(nome, fichas)
			print("Você tem 10 mil fichas para iniciar sua trajetória") # Definições iniciais# Load e save do jogo

		return (nome, fichas)

#   ========================================


sim = ["sim", "s"]  # Lista para inputs afirmativos
nao = ["nao","n","não"]  # Lista para inputs negativos
lista_arquivos = []  # Lista de jogos salvos
jogo = "jogo"
lista_jogadores = []



Joao=Jogador("joao",10000)

nome, fichas = 	Jogo.inicio() # Inicio do jogo com teste para ver se existe jogo salvo, caso contrario cria um

deck = Deck()

while True:

	print("Inicio da rodada")

	deck.shuffle()
	for i in lista_jogadores:
		i.compra_carta(deck)
		i.compra_carta(deck)
		i.mostra_mao()
	mesa = Mesa(lista_jogadores, deck)
	pot=0
	maiores_apostas=[-1]
	maior_aposta=0
	valores=[maior_aposta,pot]
	while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores):
				for i in lista_jogadores:
					valores=i.acao(valores[0],valores[1])
					try:
						maiores_apostas.remove(-1)
						if len(lista_jogadores) == 1:
							print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
							break
					except:
						if len(lista_jogadores) == 1:
							print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
							break
						continue

	tudo = mesa.flop(mesa.deck, mesa.mesa)
	maiores_apostas=[-1]
	valores[0]=0
	for i in lista_jogadores:
		i.maior_aposta=0
	for i in lista_jogadores:
		print(i.fichas)
	while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores):
			for i in lista_jogadores:
				valores=i.acao(valores[0],valores[1])
				try:
					maiores_apostas.remove(-1)
					if len(lista_jogadores) == 1:
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
				except:
					if len(lista_jogadores) == 1:
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
					continue
	tudo = mesa.turn(tudo[0], tudo[1])
	maiores_apostas=[-1]
	valores[0]=0
	for i in lista_jogadores:
		i.maior_aposta=0
	for i in lista_jogadores:
		print(i.fichas)
	while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores):
			for i in lista_jogadores:
				valores=i.acao(valores[0],valores[1])
				try:
					maiores_apostas.remove(-1)
					if len(lista_jogadores) == 1:
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
				except:
					if len(lista_jogadores) == 1:
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
					continue
	tudo = mesa.river(tudo[0], tudo[1])
	maiores_apostas=[-1]
	valores[0]=0
	for i in lista_jogadores:
		i.maior_aposta=0
	for i in lista_jogadores:
		print(i.fichas)	
	while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores):
			for i in lista_jogadores:
				valores=i.acao(valores[0],valores[1])
				try:
					maiores_apostas.remove(-1)
					if len(lista_jogadores) == 1:
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
				except:
					if len(lista_jogadores) == 1:
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
					continue


	for i in range(0,len(lista_jogadores)-1):
		lista_jogadores[i].reseta_mao()

	for i in lista_jogadores:
		i.maior_aposta=0

Jogo.fim() # Fim do jogo, salva automaticamente


print("importado")


	


	