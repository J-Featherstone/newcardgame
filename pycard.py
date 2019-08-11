import sys, random, rng, enemies, pygame, cards
from enemies import goblin
pygame.init()
rarities = {"common": (255, 255, 255), "uncommon": (0, 255, 0), "rare": (0, 0, 255), "epic": (255, 255, 0), "legendary": (0, 0, 0)}
size = width, height = 1600, 900

#I did not write this i got it from stackoverflow -> allows me to add an image background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class hand:
    max_size = 7
    cards_in_hand = []

    def draw_from_deck(self):
        drawn = deck.cards[0]
        if len(self.cards_in_hand) < 7:
            self.cards_in_hand.append(drawn)
            
        else:
            discard.discard_pile.append(drawn)

    #def check_draw(self):


	#once you have checked that the card is being clicked on this while move it around while clicked down
	#def play_card(self):

class deck:
    cards = []
    def shuffle_deck(self):
        random.shuffle(self.cards)





class discard_pile:
    cards = []

class board:
	#card info is list of [position, card_rarity, card_size]
    card_info = []
    current_enemy = goblin

    def deck_on_screen(self, cards):
        if cards:
            pygame.draw.rect(screen, (255, 97, 3), [1400, 700, 64, 89])

    def draw_board(self):
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        self.deck_on_screen(deck.cards)
        self.current_enemy.draw_enemy(screen)
        for card in self.card_info:
            pos_size = card.position + card.size
            pygame.draw.rect(screen, rarities.get(card.rarity), pos_size)
        pygame.display.update()

screen = pygame.display.set_mode(size)
BackGround = Background('wood_background.jpg', [0,0])
player_deck = deck()
player_hand = hand()
basic_attack = card()
basic_attack.position = [500, 500]
basic_attack.rarity = "common"
game_board = board()
game_board.card_info.append(basic_attack)

while (1):
    goblin.draw_enemy(screen)
    game_board.draw_board()
    basic_attack.select_card()
    basic_attack.move_card()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()