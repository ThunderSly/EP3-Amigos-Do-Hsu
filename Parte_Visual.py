import pygame as pg
import Classes_deck as Cd

#danielsc1@insper.edu.br
pg.init()

clock = pg.time.Clock()
pg.display.set_caption("Hsu Poker")
screen = pg.display.set_mode((1200,800))

grey = (200, 200, 200)
deck = Cd.Deck()
running = True
naipes = ["Copas", "Ouros", "Espadas", "Paus"]
cartas = ["A", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "J", "Q", "K"]
grafica_cartas = []

cartax = 513
cartax2 = 513
cartay = 0
cartay2 = 0

carta_oponente1x = 525
carta_oponente2x = 545		
carta_oponente1y = 100
carta_oponente2y = 100

carta_atras = pg.image.load("Sprites\\CardBack.png").convert_alpha()
carta_atras = pg.transform.scale(carta_atras,(150, 150))
music_on = True

mesa = pg.image.load("Sprites\\Mesa Insper Poker.png").convert_alpha()
mesa = pg.transform.scale(mesa,(1200, 1200))

music = pg.mixer.music.load("Sounds\\Background Music.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops = -1, start = 0.0)

botao_musica_on = Cd.Button(0, 0, 24, 16, "Sprites\\Music Button On.png", 72, 48)
botao_musica_off = Cd.Button(0, 0, 24, 16, "Sprites\\Music Button Off.png", 72, 48)

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

	if cartay < 750:
		cartay=cartay+2.5
		cartay2 = cartay2-0.15

	if cartay2 < 750:
		cartay2=cartay2+2.5
		cartax2 = cartax2+0.15

	#  =========================================================  Jogo  =======================================================================

	#  =========================================  Fundo  =====================================================================
	screen.fill(grey)

	screen.blit(mesa,(0,-100))

	# ========================= Botoes =========================================================================


	#  =====================================  Display de cartas  =============================================================
	lista_jogadores = []

	jogador = Cd.Jogador("hsu",10000)
	
	lista_jogadores= []
	deck.build()
	deck.shuffle()
	rodada = Cd.Rodada(lista_jogadores, deck)
	jogador.mao.append(deck.compra())
	# Jogaodor:
	'''screen.blit(jogador.mao[0],(cartax,cartay))
	screen.blit(jogador.mao[1],(cartax2,cartay2))

	# Oponente:
	screen.blit(carta_atras,(carta_oponente1x, carta_oponente1y))
	screen.blit(carta_atras,(carta_oponente2x,carta_oponente2y))
'''
	# Mesa:



	pg.display.update()

pg.quit()
