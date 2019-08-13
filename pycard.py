import sys, random, enemies, pygame, cards, copy
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
    cards = {}

    def draw_from_deck(self):
        drawn = deck.cards[0]
        if len(self.cards) < 7:
            self.cards_in_hand.append(drawn)
            
        else:
            discard_pile.cards.append(drawn)

    def reset_hand_position(self):
        #dist_between_cards = width / len(self.cards)
        #pressed = pygame.mouse.get_pressed()
        #if pygame.mouse.get_pressed()[0] == False:
        for key in self.cards:
            #print(ind)
            self.cards[key].position = [525 + (key * 150), 700]

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
    current_enemy = enemies.goblin

    def deck_on_screen(self, cards):
        if cards:
            pygame.draw.rect(screen, (255, 97, 3), [1400, 700, 64, 89])

    def draw_board(self, current_hand):
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        self.deck_on_screen(deck.cards)
        self.current_enemy.draw_enemy(screen)
        current_hand.reset_hand_position()
        for key, c in current_hand.cards.items():
            pos_size = c.position + c.size
            pygame.draw.rect(screen, rarities.get(c.rarity), pos_size)
        pygame.display.update()

screen = pygame.display.set_mode(size)
BackGround = Background('wood_background.jpg', [0,0])
game_board = board()
player_deck = deck()
current_hand = hand()
print(cards.basic_attack.position)
while len(current_hand.cards) < 7:
    #used copy() to stop all basic attacks inheriting the same values.
    current_hand.cards[len(current_hand.cards)] = copy.copy(cards.basic_attack)
current_hand.reset_hand_position()
#for c in current_hand.cards.items():
    #print(c)
print(current_hand.cards)

#player_hand.cards.append(cards.basic_attack)

while (1):
    goblin.draw_enemy(screen)
    game_board.draw_board(current_hand)
    cards.card.select_card(current_hand.cards)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()