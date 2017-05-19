import pygame as pg
#danielsc1@insper.edu.br
pg.init()

clock = pg.time.Clock()
pg.display.set_caption("Hsu Poker")
screen = pg.display.set_mode((800,600))

grey = (200, 200, 200)

running = True

carta = pg.image.load("Sprites\\2 de Copas.png").convert_alpha()
carta = pg.transform.scale(carta,(150,150))
cartax = 300
cartax2 = 300
cartay= -28
cartay2 = -28

music_on = True

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

	if cartay < 485:
		cartay=cartay+1.5
	if cartay2 < 485:
		cartay2=cartay2+1.5
		cartax2 = cartax2+0.15

	screen.fill(grey)
	screen.blit(carta,(cartax,cartay))
	screen.blit(carta,(cartax2,cartay2))

	pg.display.update()

pg.quit()
