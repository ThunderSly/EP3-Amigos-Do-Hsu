import pygame as pg

pg.init()

clock = pg.time.Clock()
pg.display.set_caption("Hsu Poker")
screen = pg.display.set_mode((800,600))

grey = (200, 200, 200)

running = True

carta = pg.image.load("C:\\Users\\Felippe\\Desktop\\2 de Copas.png").convert_alpha()
carta = pg.transform.scale(carta,(200,200))
cartax = 300
cartax2 = 300
cartay= -38
cartay2 = -38

while running:

	for event in pg.event.get():

		if event.type == pg.QUIT:
			running = False

	screen.fill(grey)
	screen.blit(carta,(cartax,cartay))
	screen.blit(carta,(cartax2,cartay2))
	if cartay < 450:
		cartay=cartay+1
		cartax=cartax+0.5
	if cartay2 < 450:
		cartay2=cartay2+1
		cartax2=cartax2+0.365
		
	for event in pg.event.get():

		if event.key == pg.K_r:
			cartax = 300
			cartax2 = 300
			cartay = -38
			cartay2 = -38

	pg.display.update()

pg.quit()
