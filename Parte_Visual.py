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

mesavisual = pg.image.load("Sprites\\Mesa Insper Poker.png").convert_alpha()
mesavisual = pg.transform.scale(mesavisual,(1200, 1200))

# ========================================= Music_Setup ==============================================

music = pg.mixer.music.load("Sounds\\Background Music.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops = -1, start = 0.0)
music_on = True

botao_musica_on = Cd.Button(0, 0, 24, 16, "Sprites\\Music Button On.png", 72, 48, "musica_on")
botao_musica_off = Cd.Button(0, 0, 24, 16, "Sprites\\Music Button Off.png", 72, 48, "musica_off")

# ======================================== Acao_Setup ================================================

botao_call = Cd.Button(1000, 800, 32, 12, "Sprites\\Call Button.png", 96, 36, "call")
botao_check = Cd.Button(800, 800, 38, 12, "Sprites\\Check Button.png", 114, 36, "call")
botao_raise = Cd.Button(1200, 800, 36, 12, "Sprites\\Raise Button.png", 108, 36, "call")
botao_fold = Cd.Button(800, 800, 32, 12, "Sprites\\Fold Button.png", 96, 36, "call")

while running:

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

	#  =========================================  Fundo  =====================================================================
	grey = (200, 200, 200)
	screen.fill(grey)

	screen.blit(mesavisual,(0,-200))

	#   ======================================  BOTOES ========================================================================

	#   ============ Musica ========

	#botao_musica_on.click()
	#botao_musica_off.click()

	
	if music_on == True:

		screen.blit(botao_musica_on.load(), (botao_musica_on.x, botao_musica_on.y))

		'''
	if botao_musica_on.click() == True:

		pg.mixer.music.pause()
		music_on = False
		'''

	if music_on == False:

		screen.blit(botao_musica_off.load(), (botao_musica_off.x, botao_musica_off.y))

		'''
	if botao_musica_off.click() == True:

		pg.mixer.music.unpause()
		music_on = True
	'''

		#  =====================================  Display de cartas  =============================================================
	

	while rodada:
		lista_jogadores = []
		flop = []
		turn = []
		river = []
		mesa = []
		pot = 0


		jogador = Cd.Jogador("hsu",10000)
			
		lista_jogadores= []
		deck.build()
		deck.shuffle()

		mesajogo = Cd.Mesa(deck)

		jogador.mao = jogador.compra_carta(deck)
		jogador.mao = jogador.compra_carta(deck)
		mesajogo.compra_carta(deck)

		
			# Mesa:
		maior_aposta=0
		valores=[maior_aposta,pot]
		jogador.acao(jogador.maior_aposta, pot)
		flop = (mesajogo.flop(deck, mesa))
		turn = (mesajogo.turn(deck, mesa))
		river = (mesajogo.river(deck, mesa))

		rodada = False

	# Jogaodor:

	screen.blit(jogador.mao[0].sprite, (cartax,cartay))
	screen.blit(jogador.mao[1].sprite, (cartax2,cartay2))

	# Oponente:
	
	screen.blit(carta_atras,(carta_oponente1x, carta_oponente1y))
	screen.blit(carta_atras,(carta_oponente2x, carta_oponente2y))

	# Flop:


	

	screen.blit(flop[1][0].sprite, (flop1x, flop1y))
	screen.blit(flop[1][1].sprite, (flop2x, flop2y))
	screen.blit(flop[1][2].sprite, (flop3x, flop3y))
	screen.blit(turn[1][3].sprite, (turnx, turny))
	screen.blit(turn[1][4].sprite, (riverx, rivery))

	if cartay < 600:
		cartay=cartay+2.5
		cartay2 = cartay2-0.15

	if cartay2 < 600:
		cartay2=cartay2+2.5
		cartax2 = cartax2+0.15

	pg.display.update()
	clock.tick(60)

pg.quit()