import sys, random, rng
print(sys.version, sys.path)
#import C:\Users\Joef\AppData\Python37\site-packages\pygame
import pygame
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

class card:
    #def _init_(self, rarity, cost, level):
    small_card = [64, 89]
    large_card = [small_card[0] * 2, small_card[1] * 2]
    position = []
    rarity = ""
    size = small_card
    selected = False
    #position is top left corner of card, size is small_card or large_card
    def enlarge_card(self):
        self.size = self.large_card

    def shrink_card(self):
        self.size = self.small_card

    def select_card(self):
        for index, card in enumerate(board.card_info):
            mouse_pos = pygame.mouse.get_pos()
            if card.position[0] < mouse_pos[0] < card.position[0] + card.size[0] and card.position[1] < mouse_pos[1] < card.position[1] + card.size[1]:
                self.selected = True
                self.enlarge_card()
            else:
                self.selected = False
                self.shrink_card()
    #may need to change this function to move the card while mouse is held even if mouse not inside card
    def move_card(self):
        if self.selected is True and pygame.mouse.get_pressed()[0] == True:
            self.position[0] = list(pygame.mouse.get_pos())[0] - 64
            self.position[1] = list(pygame.mouse.get_pos())[1] - 89


    def add_card(self):
        board.cards.append([self.position, self.rarity, self.size])

    #def remove_card(self):
        #board.cards.

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





class discard:
    discard_pile = []

class board:
	#card info is list of [position, card_rarity, card_size]
    card_info = []

    def deck_on_screen(self, cards):
        if cards:
            pygame.draw.rect(screen, (255, 97, 3), [1400, 700, 64, 89])

    def draw_board(self):
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        self.deck_on_screen(deck.cards)
        for card in self.card_info:
            pos_size = card.position + card.size
            pygame.draw.rect(screen, rarities.get(card.rarity), pos_size)
        pygame.display.update()


screen = pygame.display.set_mode(size)
BackGround = Background('wood_background.jpg', [0,0])
player_deck = deck()
player_hand = hand()
basic = card()
basic.position = [500, 500]
basic.rarity = "common"
game_board = board()

while (1):
    game_board.draw_board()
    basic.select_card()
    basic.move_card()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()