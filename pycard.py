import sys, pygame, random, rng
pygame.init()
colours = { "white": (255, 255, 255), "green": (0, 255, 0), "blue": (0, 0, 255), "yellow": (255, 255, 0), "black": (0, 0, 0)}
size = width, height = 1600, 1080

#I did not write this i got it from stackoverflow -> allows me to add an image background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class card:
		#def _init_(self, rarity, cost, level):
		small_card = [64, 89]
		large_card = [small_card[0] * 2, small_card[1] * 2]
		card_position = []
		rarity = ""
		size = []
		pos_rarity_size = [[],"",[]]
		#position is top left corner of card, size is small_card or large_card
		def set_position(self, x, y):
			self.card_position = [x,y]
		def set_size_small(self):
			self.size = self.small_card
		def set_size_large(self):
			self.size = self.large_card
		def set_rarity(self, rareness_str):
			self.rarity = rareness_str

		def draw_card(self, position, size, rarity):
			pos_size =  tuple(position + size)
			pygame.draw.rect(screen, colours.get(rarity), pos_size)

		def enlarge_card(self):
			mouse_pos = pygame.mouse.get_pos()
			for card in board.card_info:


		def move_card(self):
			global held, coordinates
			#while event.type == MOUSEBUTTONDOWN:
			if held:
				coordinates = pygame.mouse.get_pos()

		def add_card(self):
			board.cards.append([self.card_position, self.rarity, self.size])

		def remove_card(self):
			board.cards.


class hand:
	max_size = 5
	cards_in_hand = []
	#once you have checked that the card is being clicked on this while move it around while clicked down
	#def play_card(self):

class board:
	#card info is list of [card_position, card_rarity, card_size]
	cards = []

	def draw_board(self, card_info):
		screen.fill([255, 255, 255])
		screen.blit(BackGround.image, BackGround.rect)
		for card in card_info:
			for prs	in card:
				pos_size = prs[0] + prs[2]
				pygame.draw.rect(screen, colours.get(card_rarities[k]), pos_size)
			pygame.display.flip()


screen = pygame.display.set_mode(size)
BackGround = Background('wood_background.jpg', [0,0])
basic = card()

while (1):
	screen.fill([255, 255, 255])
	screen.blit(BackGround.image, BackGround.rect)
	basic.draw_card([800, 200], card.small_card, "white")
	pygame.display.flip()
	#if pygame.event.

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()