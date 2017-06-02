import pygame as pg
import Classes_deck as Cd
import time

class Button: # Classe de botões

	def __init__(self, x, y, w, h, sprite, xs, ys, tipo):

		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.xs = xs
		self.ys = ys
		self.sprite = sprite
		self.tipo = tipo

	def load(self): # Cartregamento da sprite do botaõ

		botao = pg.image.load(self.sprite).convert_alpha()
		botao = pg.transform.scale(botao, (self.xs, self.ys))
		self.rect = botao.get_rect()

		return botao

	def chamar_botao(self): # Utilização do botão no jogo

		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()

		if self.xs > mouse[0] > self.x and self.ys > mouse[1] > self.y :

			if click[0] == 1 :
				print("clicked")
				return True

def Detecta_botao(listaB): # Checa o uso do botão

	for i in listaB:

		if i.chamar_botao == True:

			return i.tipo

class Sprites(pg.sprite.Sprite): # Uso de sprites

	def __init__(self, imagem, x, y):
		pg.sprite.Sprite.__init__(self)
		self.imagem = pg.image.load("Sprites\\{}.png".format(imagem)).convert_alpha()
		self.imagem = pg.transform.scale(self.imagem,(x, y))
		self.retangulo = self.imagem.get_rect()

def counter(count): # Atualiza a quantidade de fichas e as mosstra na tela

	font = pg.font.SysFont(None, 25)
	text = font.render("Fichas: " + str(count), True, black)
	screen.blit(text, (10, 750))

def potcounter(pot):
	font = pg.font.SysFont(None, 25)
	text = font.render("Pot: " + str(pot), True, black)
	screen.blit(text, (1100, 10 ))

def text_objects(text, font, color): # Funcao para criar texto

	textSurface = font.render(text, True, color) # Cria um texto

	return textSurface, textSurface.get_rect() # Retorna um texto

def message_display(text, x, y, size): # Funcao que mostra um texto

	largeText = pg.font.Font("freesansbold.ttf", size) # Fonte e tamanho da fonte
	TextSurf, TextRect = text_objects(text, largeText, black) # Cria o texto chamando a funcao
	TextRect.center = ((x), (y)) # Centraliza o texto

	screen.blit(TextSurf, TextRect) # Mostra o texto na tela

	pg.display.update() # Da update na tela para aparecer o texto


black = (0, 0, 0)

sim = ["sim", "s"]  # Lista para inputs afirmativos
nao = ["nao","n","não"]  # Lista para inputs negativos

pg.init()

clock = pg.time.Clock()
pg.display.set_caption("Hsu Poker")
screen = pg.display.set_mode((1200, 800))


deck = Cd.Deck()
running = True


naipes = ["Copas", "Ouros", "Espadas", "Paus"]
cartas = ["A", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "J", "Q", "K"]
grafica_cartas = []

#  ======================================== Definição das coordenadas das cartas  =====================================================
# Localização da carta do próprio jogador
carta_oponente1x = 525 
carta_oponente2x = 545
carta_oponente1y = 100
carta_oponente2y = 100

# Localização das cartas viradas na mesa
flop1x = 340
flop1y = 320
flop2x = 440
flop2y = 320
flop3x = 540
flop3y = 320
turnx = 640
turny = 320
riverx = 740
rivery = 320

#for event in pg.event.get():
	#if event.type == MOUSEBUTTONDOWN:
        #None 




carta_atras = Sprites("CardBack", 150, 150)  # Parte de tras da carta


mesavisual = pg.image.load("Sprites\\Mesa Insper Poker.png").convert_alpha()
mesavisual = pg.transform.scale(mesavisual,(1200, 1200))

# ========================================= Music_Setup ==============================================

music = pg.mixer.music.load("Sounds\\Background Music.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops = -1, start = 0.0)
music_on = True

botao_musica_on = Button(0, 0, 24, 16, "Sprites\\Music Button On.png", 72, 48, "musica_on")
botao_musica_off = Button(0, 0, 24, 16, "Sprites\\Music Button Off.png", 72, 48, "musica_off")

# ======================================== Acao_Setup ================================================

# Caracterização do botões

botao_call = Button(800, 800, 32, 12, "Sprites\\Call Button.png", 96, 36, "call")
botao_check = Button(600, 800, 38, 12, "Sprites\\Check Button.png", 114, 36, "check")
botao_raise = Button(1000, 800, 36, 12, "Sprites\\Raise Button.png", 108, 36, "raise")
botao_fold = Button(1200, 800, 32, 12, "Sprites\\Fold Button.png", 96, 36, "fold")

lista_jogadores =[]

# Criação dos jogadores
Matilde = Cd.Bot("Matilde",10000)
jogador = Cd.Jogador("Você",10000)

lista_jogadores.append(jogador)
lista_jogadores.append(Matilde)

acao = ""
waiting = True
LEFT = 1


def tela_update(flop1,turn1,river1): # Update de display
	grey = (200, 200, 200)
	screen.fill(grey)
	screen.blit(mesavisual,(0,-200))
	screen.blit(jogador.mao[0].sprite, (cartax,cartay)) # Display das próprias cartas
	screen.blit(jogador.mao[1].sprite, (cartax2,cartay2))
	screen.blit(carta_atras.imagem,(carta_oponente1x, carta_oponente1y))
	screen.blit(carta_atras.imagem,(carta_oponente2x, carta_oponente2y))

	screen.blit(botao_check.load(), (400, 700))   # Display dos botões
	screen.blit(botao_call.load(), (600, 700))
	screen.blit(botao_raise.load(), (800, 700))
	screen.blit(botao_fold.load(), (1000, 700))
	screen.blit(botao_musica_on.load(), (botao_musica_on.x, botao_musica_on.y))
	counter(jogador.fichas)
	potcounter(valores[1])

	if river1 == True:
		screen.blit(river[1][0].sprite, (flop1x, flop1y))
		screen.blit(river[1][1].sprite, (flop2x, flop2y))
		screen.blit(river[1][2].sprite, (flop3x, flop3y))
		screen.blit(river[1][3].sprite, (turnx, turny))
		screen.blit(river[1][4].sprite, (riverx, rivery))

	elif turn1 == True:
		screen.blit(turn[1][0].sprite, (flop1x, flop1y))
		screen.blit(turn[1][1].sprite, (flop2x, flop2y))
		screen.blit(turn[1][2].sprite, (flop3x, flop3y))
		screen.blit(turn[1][3].sprite, (turnx, turny))

	elif flop1 == True:
		screen.blit(flop[1][0].sprite, (flop1x, flop1y))
		screen.blit(flop[1][1].sprite, (flop2x, flop2y))
		screen.blit(flop[1][2].sprite, (flop3x, flop3y))
	pg.display.update()




while running: # Caracterização do fechamento de janelas e da tecla que liga e desliga a musica
	rodada = True
	flop1=False
	turn1=False
	river1=False
	for event in pg.event.get():

		if event.type == pg.QUIT:
			running = False

		if event.type == pg.KEYDOWN:

			if event.key == pg.K_m and music_on == True:

				pg.mixer.music.pause()
				music_on = False

			elif event.key == pg.K_m and music_on == False:

				pg.mixer.music.unpause()
				music_on = True
		



	#  =========================================================  Jogo  =======================================================================

	#  =========================================  Fundo e mesa =====================================================================
	grey = (200, 200, 200)
	screen.fill(grey)

	screen.blit(mesavisual,(0,-200))

	#   ======================================  BOTOES ========================================================================



	botao_check_click = botao_check.chamar_botao()
	botao_call_click = botao_call.chamar_botao()
	botao_raise_click = botao_raise.chamar_botao()
	botao_fold_click = botao_fold.chamar_botao()


	#   ============ Musica ========

	# Funcionalidade do botão que controla a musica 

	botao_musica_on.chamar_botao()
	botao_musica_off.chamar_botao()

	
	if music_on == True:

		screen.blit(botao_musica_on.load(), (botao_musica_on.x, botao_musica_on.y))

		
	if botao_musica_on.chamar_botao() == True:

		pg.mixer.music.pause()
		music_on = False
		

	if music_on == False:

		screen.blit(botao_musica_off.load(), (botao_musica_off.x, botao_musica_off.y))

		
	if botao_musica_off.chamar_botao() == True:

		pg.mixer.music.unpause()
		music_on = True
	
	pg.display.update()



		#  =====================================  Display de cartas  =============================================================
	

	while rodada: #Início da rodada

		if Matilde not in lista_jogadores:
			lista_jogadores.append(Matilde)
		if jogador not in lista_jogadores:
			lista_jogadores.append(jogador)


		for event in pg.event.get(): # Checa a utilização dos botões

			if event.type == pg.QUIT:
				running = False

			if event.type == pg.KEYDOWN:

				if event.key == pg.K_m and music_on == True:

					pg.mixer.music.pause()
					music_on = False

				elif event.key == pg.K_m and music_on == False:

					pg.mixer.music.unpause()
					music_on = True



		#Posição das cartas
		cartax = 513
		cartax2 = 513
		cartay = 0
		cartay2 = 0
		valores = []

		flop = []
		turn = []
		river = []
		mesa = []
		pot = 0
		jogador.mao = []
		mesajogo = []

			
		deck.shuffle()  # Embaralha as cartas

		mesajogo = Cd.Mesa(deck)
		jogador.mao = jogador.compra_carta(deck) # Jogador compra as cartas
		jogador.mao = jogador.compra_carta(deck)
	
		Matilde.mao = Matilde.compra_carta(deck) # Bot compra as cartas
		Matilde.mao = Matilde.compra_carta(deck)



		while cartay < 600 and cartay2 < 600: # Alteração da posição das próprias cartas


			screen.fill(grey) # Atualização do fundo cinza

			screen.blit(mesavisual,(0,-200)) # Atualização do display da mesa

			screen.blit(jogador.mao[0].sprite, (cartax,cartay)) # Display das próprias cartas
			screen.blit(jogador.mao[1].sprite, (cartax2,cartay2))
			screen.blit(carta_atras.imagem,(carta_oponente1x, carta_oponente1y))
			screen.blit(carta_atras.imagem,(carta_oponente2x, carta_oponente2y))
			# Muda as cartas de lugar
			cartay=cartay+2.5
			cartay2 = cartay2-0.15
			

			cartay2=cartay2+2.65
			cartax2 = cartax2+0.15

			pg.display.update()

		screen.blit(botao_check.load(), (400, 700))   # Display dos botões
		screen.blit(botao_call.load(), (600, 700))
		screen.blit(botao_raise.load(), (800, 700))
		screen.blit(botao_fold.load(), (1000, 700))

		counter(jogador.fichas)
		potcounter(pot)
		pg.display.update()

			# Mesa:
		maior_aposta=0
		maiores_apostas=[-1]
		valores=[maior_aposta,pot,maiores_apostas,lista_jogadores]

		while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores): 
			potcounter(valores[1])
			counter(jogador.fichas)

			for i in lista_jogadores:
				
				if i != Matilde:
					while True:

						event = pg.event.wait() # Aguarda um comando do jogador


						if event.type == pg.QUIT:
							pg.quit()

						if event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:

							mouse = pg.mouse.get_pos()
							click = pg.mouse.get_pressed()

							if 514 > mouse[0] > 400 and 736 > mouse[1] > 700 :

									acao = "check" # Clique de check

						if event.type == pg.KEYDOWN:

							if event.key == pg.K_c and i.maior_aposta==0:
								acao = "check"
								print("click")# Clique de check
								break
								
							if event.key == pg.K_j and i.maior_aposta==0:
								acao = "call"
								print("click")# Clique de call
								break

							if event.key == pg.K_r:
								acao = "raise"
								print("click")# Clique de raise
								break

							if event.key == pg.K_f:
								acao = "fold"
								print("click")# Clique de fold
								break
				


					valores = i.acao(valores[0], valores[1], acao, valores[2],valores[3]) # Realiza a ação pedida

					tela_update(flop1,turn1,river1)
					print(maiores_apostas)
					print(valores[3])
					
				elif i == Matilde:
					valores= i.acaox(valores[0],valores[1],mesa,valores[2],valores[3]) # Ação do bot
					print(maiores_apostas)
					print(valores[3])
					time.sleep(1.5)
					tela_update(flop1,turn1,river1)
				try:
					maiores_apostas.remove(-1) # Checa apostas
					if len(valores[3]) == 1:
						print(valores[3])
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						lista_jogadores[0].fichas+=valores[1]
						break
				except:
					if len(valores[3]) == 1:
						print(valores[3])
						print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						lista_jogadores[0].fichas+=valores[1]
						break
					continue

				counter(jogador.fichas)
			if len(valores[3]) == 1:
				break

		print(valores[3])

		if len(valores[3]) == 1:
			break
		maiores_apostas1=[-1]
		valores[0]=0
		valores[2]=maiores_apostas1
		for i in lista_jogadores:
			i.maior_aposta=0		
		print(maiores_apostas1)

		flop = (mesajogo.flop(deck, mesa)) # Realização do Flop
		screen.blit(flop[1][0].sprite, (flop1x, flop1y))
		screen.blit(flop[1][1].sprite, (flop2x, flop2y))
		screen.blit(flop[1][2].sprite, (flop3x, flop3y))
		pg.display.update() # Atualização da tela
		flop1=True

		while maiores_apostas1.count(max(maiores_apostas1)) != len(lista_jogadores):


				for i in lista_jogadores: # Realiza novamente o aguardo de uma ação
						print(maiores_apostas1)
						if i != Matilde:
							while True:


								event = pg.event.wait()


								if event.type == pg.QUIT:
									pg.quit()
								if event.type == pg.KEYDOWN:

									if event.key == pg.K_c and i.maior_aposta==0:
										acao = "check"
										print("click")
										break
										
									if event.key == pg.K_j and i.maior_aposta==0:
										acao = "call"
										print("click")
										break

									if event.key == pg.K_r:
										acao = "raise"
										print("click")
										break

									if event.key == pg.K_f:
										acao = "fold"
										print("click")
										break

							valores = i.acao(valores[0], valores[1], acao, valores[2],valores[3]) # Realiza a ação
							tela_update(flop1,turn1,river1)
							print(maiores_apostas1)							
							print(valores[3])
						

						elif i == Matilde:
							valores = i.acaox(valores[0],valores[1], flop[1], valores[2],valores[3]) # Ação do Bot
							time.sleep(1.5)
							tela_update(flop1,turn1,river1)
							print(maiores_apostas1)
							print(valores[3])

						try:
							maiores_apostas1.remove(-1)
							if len(valores[3]) == 1:
								print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
								lista_jogadores[0].fichas+=valores[1]
								break

						except:
							if len(valores[3]) == 1:
								print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
								lista_jogadores[0].fichas+=valores[1]
								break
							continue

						counter(jogador.fichas)

		print(lista_jogadores)

		if len(lista_jogadores) == 1:
			break
		maiores_apostas2=[-1]
		valores[0]=0
		valores[2]=maiores_apostas2

		for i in lista_jogadores:
			i.maior_aposta=0		
		turn = (mesajogo.turn(flop[0], flop[1]))
		screen.blit(turn[1][3].sprite, (turnx, turny)) # Abre as carta do turn
		pg.display.update() # Atualiza a tela
		turn1=True
		while maiores_apostas2.count(max(maiores_apostas2)) != len(lista_jogadores): # Aguarda ação do river


				for i in lista_jogadores:
						print(maiores_apostas2)
						if i != Matilde:
							while True:

								event = pg.event.wait()

								if event.type == pg.QUIT:
									pg.quit()
								if event.type == pg.KEYDOWN:

									if event.key == pg.K_c and i.maior_aposta==0:
										acao = "check"
										print("click")
										break
										
									if event.key == pg.K_j and i.maior_aposta==0:
										acao = "call"
										print("click")
										break

									if event.key == pg.K_r:
										acao = "raise"
										print("click")
										break

									if event.key == pg.K_f:
										acao = "fold"
										print("click")
										break


							valores = i.acao(valores[0], valores[1], acao, valores[2],lista_jogadores)
							lista_jogadores=valores[3]
							tela_update(flop1,turn1,river1)
							print(maiores_apostas2)
							print(lista_jogadores)

						elif i == Matilde:
							valores=i.acaox(valores[0],valores[1], turn[1], valores[2],lista_jogadores)
							time.sleep(1.5)
							tela_update(flop1,turn1,river1)
							print(maiores_apostas2)
							print(lista_jogadores)
						try:
							maiores_apostas2.remove(-1)
							if len(lista_jogadores) == 1:
								print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
								lista_jogadores[0].fichas+=valores[1]
								break
						except:
							if len(lista_jogadores) == 1:
								print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
								lista_jogadores[0].fichas+=valores[1]
								break
							continue

						counter(jogador.fichas) # Conta as fichas

		print(lista_jogadores)

		if len(lista_jogadores) == 1:
			break
		maiores_apostas3=[-1]
		valores[2]=maiores_apostas3
		valores[0]=0

		for i in lista_jogadores:
			i.maior_aposta=0		
		river = (mesajogo.river(turn[0], turn[1]))
		screen.blit(river[1][4].sprite, (riverx, rivery)) # Vira a carta do river
		pg.display.update()
		river1=True
		while maiores_apostas3.count(max(maiores_apostas3)) != len(lista_jogadores): # Verifica a ultima vez a ação do jogador
				for i in lista_jogadores:
						print(maiores_apostas3)
						if i != Matilde:
							while True:


								event = pg.event.wait()

								if event.type == pg.QUIT:
									pg.quit()
								if event.type == pg.KEYDOWN:

									if event.key == pg.K_c and i.maior_aposta==0:
										acao = "check"
										print("click")
										break
										
									if event.key == pg.K_j and i.maior_aposta==0:
										acao = "call"
										print("click")
										break

									if event.key == pg.K_r:
										acao = "raise"
										print("click")
										break

									if event.key == pg.K_f:
										acao = "fold"
										print("click")
										break
							valores = i.acao(valores[0],valores[1],acao,valores[2],lista_jogadores)						
							tela_update(flop1,turn1,river1)
							print(maiores_apostas3)
							print(lista_jogadores)
						elif i == Matilde:
							valores = i.acaox(valores[0],valores[1], river[1], valores[2],lista_jogadores)
							time.sleep(1.5)
							tela_update(flop1,turn1,river1)
							print(maiores_apostas3)
							print(lista_jogadores)
						try:
							maiores_apostas3.remove(-1)
							if len(lista_jogadores) == 1:
								print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
								lista_jogadores[0].fichas+=valores[1]
								break
						except:
							if len(lista_jogadores) == 1:
								print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
								lista_jogadores[0].fichas+=valores[1]
								break
							continue

						counter(jogador.fichas)
		if len(lista_jogadores) == 1:
			break
		print(lista_jogadores)
		comp = Cd.Compara_Maos.peneira(river[1],lista_jogadores) # Realiza a peneira e checa quem ganhou
		comp.fichas += valores[1]
		message_display("{} ganhou! Deseja começar uma nova rodada?".format(comp.nome), 400, 50, 20)

		for i in range(0,len(lista_jogadores)):
			lista_jogadores[i].reseta_mao() # Limpa a mão dos jogadores
		for i in lista_jogadores:
			i.maior_aposta=0
			print(i.fichas) #Fichas

		acao=0
		rodada = False



	

	pg.display.update()
	clock.tick(15)
	novarodada=False
	print("Deseja começar uma nova rodada?")  # Pergunta se deseja uma nova rodada
	while True:
		event = pg.event.wait()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_s:
				print(sim)
				novarodada=True
				break		
			if event.key == pg.K_n and i.maior_aposta==0:
				print(nao)
				novarodada=False
				break
	if novarodada==True:
		continue
	elif novarodada==False:
		break
pg.quit()