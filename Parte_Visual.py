import pygame as pg
import Classes_deck as Cd

#danielsc1@insper.edu.br
pg.init()

clock = pg.time.Clock()
pg.display.set_caption("Hsu Poker")
screen = pg.display.set_mode((1200, 800))


deck = Cd.Deck()
running = True
rodada = True

naipes = ["Copas", "Ouros", "Espadas", "Paus"]
cartas = ["A", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "J", "Q", "K"]
grafica_cartas = []

carta_oponente1x = 525
carta_oponente2x = 545
carta_oponente1y = 100
carta_oponente2y = 100

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


cartax = 513
cartax2 = 513
cartay = 0
cartay2 = 0

carta_atras = pg.image.load("Sprites\\CardBack.png").convert_alpha()
carta_atras = pg.transform.scale(carta_atras,(150, 150))
music_on = True

mesavisual = pg.image.load("Sprites\\Mesa Insper Poker.png").convert_alpha()
mesavisual = pg.transform.scale(mesavisual,(1200, 1200))

music = pg.mixer.music.load("Sounds\\Background Music.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops = -1, start = 0.0)


while running:

	for event in pg.event.get():

		if event.type == pg.QUIT:
			running = False

		if event.type == pg.KEYDOWN:

				
			if event.key == pg.K_r:
				cartax = 300
				cartax2 = 300
				cartay = -38
				cartay2 = -38

			if event.key == pg.K_m and music_on == True:

				pg.mixer.music.pause()
				music_on = False

			elif event.key == pg.K_m and music_on == False:

				pg.mixer.music.unpause()
				music_on = True



	#  =========================================================  Jogo  =======================================================================

	#  =========================================  Fundo  =====================================================================
	grey = (200, 200, 200)
	screen.fill(grey)

	screen.blit(mesavisual,(0,-200))

		#  =====================================  Display de cartas  =============================================================
	

	while rodada:
		lista_jogadores = []
		flop = []
		turn = []
		river = []
		mesa = []


		jogador = Cd.Jogador("hsu",10000)
		jogador1 = Cd.Jogador("brunao",10000)

		deck.build()
		deck.shuffle()

		mesajogo = Cd.Mesa(deck)
		jogador.mao = jogador.compra_carta(deck)
		jogador.mao = jogador.compra_carta(deck)
		screen.blit(jogador.mao[0].sprite, (cartax,cartay))
		screen.blit(jogador.mao[1].sprite, (cartax2,cartay2))
		screen.blit(carta_atras,(carta_oponente1x, carta_oponente1y))
		screen.blit(carta_atras,(carta_oponente2x, carta_oponente2y))
		pg.display.update()
		if cartay < 600:
			cartay=cartay+2.5
			cartay2 = cartay2-0.15

		if cartay2 < 600:
			cartay2=cartay2+2.5
			cartax2 = cartax2+0.15
			# Mesa:
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
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
				except:
					if len(lista_jogadores) == 1:
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
					continue
		
		flop = mesajogo.flop(mesajogo.deck, mesajogo.mesa)
		screen.blit(flop[1][0].sprite, (flop1x, flop1y))
		screen.blit(flop[1][1].sprite, (flop2x, flop2y))
		screen.blit(flop[1][2].sprite, (flop3x, flop3y))
		pg.display.update()
		maiores_apostas=[-1]
		valores[0]=0
		for i in lista_jogadores:
			i.maior_aposta=0
		while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores):
			for i in lista_jogadores:
				valores=i.acao(valores[0],valores[1])
				try:
					maiores_apostas.remove(-1)
					if len(lista_jogadores) == 1:
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
				except:
					if len(lista_jogadores) == 1:
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
					continue
		
		turn = mesajogo.turn(flop[0], flop[1])
		screen.blit(turn[1][3].sprite, (turnx, turny))
		pg.display.update()
		maiores_apostas=[-1]
		valores[0]=0
		for i in lista_jogadores:
			i.maior_aposta=0
		while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores):
			for i in lista_jogadores:
				valores=i.acao(valores[0],valores[1])
				try:
					maiores_apostas.remove(-1)
					if len(lista_jogadores) == 1:
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
				except:
					if len(lista_jogadores) == 1:
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
					continue
		
		river = mesajogo.river(turn[0], turn[1])
		screen.blit(river[1][4].sprite, (riverx, rivery))
		pg.display.update()
		maiores_apostas=[-1]
		valores[0]=0
		for i in lista_jogadores:
			i.maior_aposta=0
		while maiores_apostas.count(max(maiores_apostas)) != len(lista_jogadores):
			for i in lista_jogadores:
				valores=i.acao(valores[0],valores[1])
				try:
					maiores_apostas.remove(-1)
					if len(lista_jogadores) == 1:
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
				except:
					if len(lista_jogadores) == 1:
						#print("{} ganhou {} fichas!".format(lista_jogadores[0].nome, valores[1]))
						break
					continue
		
		for i in range(0,len(lista_jogadores)-1):
			lista_jogadores[i].reseta_mao()
		for i in lista_jogadores:
			i.maior_aposta=0


		rodada = False

	# Jogaodor:



	# Oponente:
	


	# Flop:


	









pg.quit()
