import pygame as pg

pg.init()

class Button:

	def __init__(self, x, y, w, h, sprite, xs, ys, tipo):

		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.xs = xs
		self.ys = ys
		self.sprite = sprite
		self.tipo = tipo

	def load(self):

		botao = pg.image.load(self.sprite).convert_alpha()
		botao = pg.transform.scale(botao, (self.xs, self.ys))

		return botao

	def chamar_botao(self):

		mouse = pg.mouse.get_pos()
		click = pg.mouse.get_pressed()

		if self.xs > mouse[0] > self.x and self.ys > mouse[1] > self.y :

			if click[0] == 1 :
				print("clicked")
				return True

clock = pg.time.Clock()
pg.display.set_caption("Hsu Poker")
screen = pg.display.set_mode((200, 200))

botao_teste = Button(0, 0, 32, 12, "Sprites\\Call Button.png", 96, 36, "call")

white = (255, 255, 255)
black = (0, 0, 0)

running = True

b = False

while running:

	for event in pg.event.get():

		if event.type == pg.QUIT:

			running = False

		print(event)

	screen.blit(botao_teste.load(), (0,0))

	a = botao_teste.chamar_botao()

	if a == True and b == False:

		b = True

		screen.fill(white)

	elif a == True and b == True:

		b = False

		screen.fill(black)

	pg.display.update()
	clock.tick(15)
