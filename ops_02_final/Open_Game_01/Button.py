import pygame

pygame.display.set_caption('Adventure for A+')
class Button_start:
	def __init__(self, text, width, height, pos, elevation):
		#Core attributes
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle
		self.top_rect = pygame.Rect(pos, (width, height))
		self.top_color = '#475F77'

		# bottom rectangle
		self.bottom_rect = pygame.Rect(pos, (width, height))
		self.bottom_color = '#354B5E'
		#text
		self.text_surf = game_font_s.render(text, True, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

	def draw(self):
		# elevation logic
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
		pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					from main_map import runMap
					runMap()
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'


class Button_howto:       # 나중에 수정하기
	def __init__(self, text, width, height, pos, elevation):
		#Core attributes
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle
		self.top_rect = pygame.Rect(pos, (width, height))
		self.top_color = '#475F77'

		# bottom rectangle
		self.bottom_rect = pygame.Rect(pos, (width, height))
		self.bottom_color = '#354B5E'
		#text
		self.text_surf = game_font_s.render(text, True, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

	def draw(self):
		# elevation logic
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
		pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					from Pause import pause_Howto
					pause_Howto()
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'


class Button_quit:       # 나중에 수정하기
	def __init__(self, text, width, height, pos, elevation):
		#Core attributes
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		# top rectangle
		self.top_rect = pygame.Rect(pos, (width, height))
		self.top_color = '#475F77'

		# bottom rectangle
		self.bottom_rect = pygame.Rect(pos, (width, height))
		self.bottom_color = '#354B5E'
		#text
		self.text_surf = game_font_s.render(text, True, '#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

	def draw(self):
		# elevation logic
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
		pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					pygame.quit()
					quit()
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'


pygame.init()
start_page = pygame.image.load('images/start.png')
start_page = pygame.transform.scale(start_page, (800, 600))
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
game_font_s = pygame.font.Font("Marvel-Regular.ttf", 30)

button_start = Button_start('Play', 200, 40, (300, 300), 5)
button_howto = Button_howto('How to', 200, 40, (300, 370), 5)
button_quit = Button_quit('quit', 200, 40, (300, 440), 5)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	screen.blit(start_page, (0, 0))
	# screen.fill('#DCDDD8')
	button_start.draw()
	button_howto.draw()
	button_quit.draw()

	pygame.display.update()
	clock.tick(60)
