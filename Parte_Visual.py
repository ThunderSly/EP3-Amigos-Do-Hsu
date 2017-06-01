import pygame as pg
import Classes_deck as Cd

class Button:

	def __init__(self, x, y, w, h, sprite, xs, ys):

		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.xs = xs
		self.ys = ys
		self.sprite = sprite

	def load(self):

		botao = pg.image.load(self.sprite).convert_alpha()
		botao = pg.transform.scale(botao, (self.xs, self.ys))
		self.rect = botao.get_rect()

		return botao

	def chamar_botao(self):
		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()

		if self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y :

			if click[0] == 1 :
				print("clicked")
				return True

class Sprites(pg.sprite.Sprite):
	def __init__(self, imagem, x, y):
		pg.sprite.Sprite.__init__(self)
		self.imagem = pg.image.load("Sprites\\{}.png".format(imagem)).convert_alpha()
		self.imagem = pg.transform.scale(self.imagem,(x, y))
		self.retangulo = self.imagem.get_rect()

#danielsc1@insper.edu.br

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




carta_atras = Sprites("CardBack", 150, 150)
#carta_atras = pg.image.load("Sprites\\CardBack.png").convert_alpha()
#carta_atras = pg.transform.scale(carta_atras,(150, 150))

mesavisual = pg.image.load("Sprites\\Mesa Insper Poker.png").convert_alpha()
mesavisual = pg.transform.scale(mesavisual,(1200, 1200))

# ========================================= Music_Setup ==============================================

music = pg.mixer.music.load("Sounds\\Background Music.mp3")
pg.mixer.music.set_volume(0.2)
pg.mixer.music.play(loops = -1, start = 0.0)
music_on = True

botao_musica_on = Button(0, 0, 24, 16, "Sprites\\Music Button On.png", 72, 48)
botao_musica_off = Button(0, 0, 24, 16, "Sprites\\Music Button Off.png", 72, 48)

# ======================================== Acao_Setup ================================================

botao_call = Button(1000, 800, 32, 12, "Sprites\\Call Button.png", 96, 36)
botao_check = Button(800, 800, 38, 12, "Sprites\\Check Button.png", 114, 36)
botao_raise = Button(1200, 800, 36, 12, "Sprites\\Raise Button.png", 108, 36)
botao_fold = Button(800, 800, 32, 12, "Sprites\\Fold Button.png", 96, 36)

lista_jogadores =[]

jogador = Cd.Jogador("hsu",10000)
Matilde = Cd.Bot("Matilde",10000)
lista_jogadores.append(jogador)
lista_jogadores.append(Matilde)


while running:
	rodada = True

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
	
	pg.display.flip()

		#  =====================================  Display de cartas  =============================================================
	

	while rodada:
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

			
		deck.build()
		deck.shuffle()

		mesajogo = Cd.Mesa(deck)
		jogador.mao = jogador.compra_carta(deck)
		jogador.mao = jogador.compra_carta(deck)

		mesajogo.compra_carta(deck)		


		while cartay < 600 and cartay2 < 600:
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

			screen.fill(grey)

			screen.blit(mesavisual,(0,-200))

			screen.blit(carta_atras.imagem,(carta_oponente1x, carta_oponente1y))
			screen.blit(carta_atras.imagem,(carta_oponente2x, carta_oponente2y))
			screen.blit(jogador.mao[0].sprite, (cartax,cartay))
			screen.blit(jogador.mao[1].sprite, (cartax2,cartay2))

			
			cartay=cartay+2.5
			cartay2 = cartay2-0.15
			

			cartay2=cartay2+2.65
			cartax2 = cartax2+0.15
				


			pg.display.update()


			# Mesa:
		maior_aposta=0
		valores=[maior_aposta,pot]
		

		Matilde.acaox(Matilde.maior_aposta,pot,mesa)

		acao=input("Call(C), Raise(R), Fold(F)\n").lower()
		jogador.acao(jogador.maior_aposta, pot, acao)
		flop = (mesajogo.flop(deck, mesa))
		screen.blit(flop[1][0].sprite, (flop1x, flop1y))
		screen.blit(flop[1][1].sprite, (flop2x, flop2y))
		screen.blit(flop[1][2].sprite, (flop3x, flop3y))
		pg.display.flip()

		Matilde.acaox(Matilde.maior_aposta,pot,flop[1])

		acao=input("Call(C), Raise(R), Fold(F)\n").lower()
		jogador.acao(jogador.maior_aposta, pot, acao)
		turn = (mesajogo.turn(deck, mesa))
		screen.blit(turn[1][3].sprite, (turnx, turny))
		pg.display.flip()

		Matilde.acaox(Matilde.maior_aposta,pot,turn[1])

		acao=input("Call(C), Raise(R), Fold(F)\n").lower()
		jogador.acao(jogador.maior_aposta, pot, acao)
		river = (mesajogo.river(deck, mesa))
		screen.blit(river[1][4].sprite, (riverx, rivery))
		pg.display.flip()

		comp = Cd.Compara_Maos.peneira(river[1],lista_jogadores)
		comp.fichas += valores[1]
		print("{} ganhou!".format(comp.nome))

		for i in range(0,len(lista_jogadores)):
			lista_jogadores[i].reseta_mao()
		for i in lista_jogadores:
			i.maior_aposta=0
			print(i.fichas)

		rodada = False



	

	pg.display.update()
	clock.tick(60)

	novarodada = input("Deseja começar uma nova rodada?")
	if novarodada in sim:
		continue
	if novarodada in nao:
		break

pg.quit()