import itertools
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
		naipes=["Ouros","Paus","Copas","Espadas"]
		
		for i in naipes:

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

	def __init__(self,nome,fichas,xp): # Define o nome do jogador, suas cartas e a quantidade de fichas disponíveis

		self.nome = nome
		self.mao = []
		self.fichas = fichas
		self.xp=xp
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


	def Melhor_mao(jogador):	
		
		
		cartas_jogadores=mesa + jogador.mao
		lista_valores=[]
		lista_naipes=[]
		combinacoes=[]
		valor_mao=0

		for i in cartas_jogadores:
			lista_valores.append(i.valor)
			lista_naipes.append(i.naipe)
			if i.valor==1:
				lista_valores.append(14) # valores das cartas
				lista_naipes.append(i.naipe) #naipes das cartas
			
		for i in lista_valores: #para definir pares,trincas e quadras
							
			if lista_valores.count(i)==4: # Quadra
				for x in range(8):
					combinacoes.append(i)
							
			elif lista_valores.count(i)==3:
				combinacoes.append(i)

			elif lista_valores.count(i)==2:
				combinacoes.append(i)

		combinacoes.sort()

		if combinacoes[0]==combinacoes[1] and combinacoes[2]==combinacoes[3] and combinacoes[4]==combinacoes[5]: #retirar o terceiro par
			if combinacoes[0]!=combinacoes[2]:
				del combinacoes[0]
				del combinacoes[0]

		if len(combinacoes) == 2: # Par
			print("Par de {}".format(i))
			valor_mao=2			
			
		if len(combinacoes) == 4: # Dois Pares
			print("Dois pares de {} e de {}".format(combinacoes[0],combinacoes[2]))
			valor_mao=3
			
		if len(combinacoes) == 3: # Trinca
			print("Trinca de {}".format(i))
			valor_mao=4

		for n in range(1,11): 				
			if n in lista_valores: #Straight
				if n+1 in lista_valores:
					if n+2 in lista_valores:
						if n+3 in lista_valores:
							if n+4 in lista_valores:
								print("Straight de {} a {}".format(n,n+4))
								valor_mao=5

		for i in lista_naipes: 
			if lista_naipes.count(i)>=5: #Flush
				print("Flush de {}".format(i))
				valor_mao=6
			
		if len(combinacoes) == 5 or len(combinacoes) == 6: # Full House
			print("Full House")
			valor_mao=7
			
		elif len(combinacoes) >= 7: #Quadra
			valor_mao=8

		for n in range(1,11): # Straight Flush				
			for c in lista_naipes:
				if cartas_jogadores(n,c) and cartas_jogadores(n+1,c) and cartas_jogadores(n+2,c) and cartas_jogadores(n+3,c) and cartas_jogadores(n+4,c) in lista_valores:
					print("Straight Flush")
					valor_mao=9
					if n==10: #Royal Straight Flush
						valor_mao=10

	def Maos_iguais(self,valor_mao):
		valor_especifico=0
		if valor_mao==0: #pega a melhor carta
			valor_especifico=max(lista_valores)

		elif valor_mao==2: #pega o valor do par
			for i in lista_valores:
				if lista_valores.count(i)==2:
					valor_especifico=i

		elif valor_mao==3: #pega o valor do maior par
			maior=[]
			for i in lista_valores:
				if lista_valores.count(i)==2:
					maior.append(i)
			valor_especifico=max(maior)

		elif valor_mao==4: #pega o valor da trinca
			for i in lista_valores:
				if lista_valores.count(i)==3:
					valor_especifico=i

		elif valor_mao==5: #pega o valor do primeiro membro do Straight (final)
			for n in range(1,11):
				if n in lista_valores:
					if n+1 in lista_valores:
						if n+2 in lista_valores:
							if n+3 in lista_valores:
								if n+4 in lista_valores:
									valor_especifico=n+4

		elif valor_mao==6: #pega o valor do maior membro do Flush
			maior=[]
			for x in lista_naipes:
				if lista_naipes.count(x)>=5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			valor_especifico=max(maior)

		elif valor_mao==7: #pega o valor da trinca do Full House
			for i in lista_valores:
				if lista_valores.count(i)==3:
					valor_especifico=i
					break

		elif valor_mao==8: #pega o valor da quadra
			for i in lista_valores:
				if lista_valores.count(i)==4:
					valor_especifico=i
					break

		elif valor_mao==9: #pega o valor do Straight Flush (final)
			maior=[]
			for x in lista_naipes:
				if lista_naipes.count(x)>=5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			valor_especifico=max(maior)

	def Carta_a_Carta_1(self,valor_mao):
		if valor_mao==0: #pega o valor da segunda maior carta
			maior=[]
			for x in lista_valores:
				maior.append(x)
			maior.sort(reverse=True)
			valor_especifico=maior[1]

		elif valor_mao==2: #pega o valor da melhor carta fora o par
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)!=2:	
					maior.append(x)
			valor_especifico=max(maior)

		elif valor_mao==3: #pega o valor do menor par
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)==2:
					maior.append(x)
			valor_especifico=min(maior)

		elif valor_mao==4: #pega o valor da maior carta fora a trinca
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)!=3:
					maior.append(x)
			valor_especifico=max(maior)

		elif valor_mao==6: #pega o valor da segunda maior carta do Flush
			maior=[]
			for x in lista_naipes:
				if lista_naipes.count(x)>=5:
					for i in cartas_jogadores:
						if i.naipe == x:
							maior.append(i.valor)
					break
			maior.sort(reverse=True)
			valor_especifico=maior[1]

		elif valor_mao==7: #pega o valor do par do Full House (final)
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)==2:
					maior.append(x)
			valor_especifico=max(maior)

		elif valor_mao==8: #pega o valor da melhor carta fora a quadra (final)
			maior=[]
			for x in lista_valores:
				if lista_valores.count(x)!=4:
					maior.append(x)
			valor_especifico=max(maior)

	def Carta_a_Carta_2(self,valor_mao):

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

	def Carta_a_Carta_3(self,valor_mao):

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

	def Carta_a_Carta_4(self,valor_mao):

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



class Carregamento:

	def salvar():  # Função de salvar o jogo

		dados= open(jogo,'wb') 
		pickle.dump({"{}".format(jogo) : [nome, fichas, xp ]}, dados)
		dados.close()
		time.sleep(0.5)
		print("Jogo salvo com sucesso!")

	def load():

		try: # Traz o jogo salvo com os dados guardados
			dado=pickle.load(open(jogo,"rb"))  
			nome=dado["{}".format(jogo)][0]
			fichas=dado["{}".format(jogo)][1]
			xp=dado["{}".format(jogo)][2]
			carregado=sim
			Jogador(nome, fichas,xp)
			time.sleep(2)
			print("O nome do seu personagem é {}, você possui {} de fichas e {} de experiência" .format(nome,fichas,xp)) # Caracterização dos dados para o usuário

		except: # Cria um novo personagem
			dados= open(jogo,'wb')
			time.sleep(0.5)
			dados.close()
			nome=input("Qual vai ser o nome do seu personagem?\n")
			fichas= 10000
			xp=0
			Jogador(nome, fichas,xp)
			print("Você tem 10 mil fichas para iniciar sua trajetória") # Definições iniciais

class Jogo:

	def inicio():
		print("Bem vindo ao Hsu Poker! ") # Começo do jo
		Carregamento.load()

	def fim():
		Carregamento.salvar()
		time.sleep(0.5)
		print("Até a próxima!") # Finalização do jogo

#   ========================================


sim=["sim", "s"]  # Lista para inputs afirmativos
nao=["nao","n","não"]  # Lista para inputs negativos
lista_arquivos=[]  # Lista de jogos salvos


	




