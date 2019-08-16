import pygame
pygame.font.init()
class card:
    #def _init_(self, rarity, cost, level):
    small_card = [64, 89]
    large_card = [small_card[0] * 2, small_card[1] * 2]
    position = []
    rarity = ""
    size = small_card
    selected = False
    attack = 0
    block = 0
    card_name = ""
    #position is top left corner of card, size is small_card or large_card
    def enlarge_card(self):
        self.size = self.large_card

    def shrink_card(self):
        self.size = self.small_card

    def select_card(self, cards):
        for index, card in cards:
            mouse_pos = pygame.mouse.get_pos()
            if card.position[0] < mouse_pos[0] < card.position[0] + card.size[0] and card.position[1] < mouse_pos[1] < card.position[1] + card.size[1]:
                self.selected = True
                self.enlarge_card()
            else:
                self.selected = False
                self.shrink_card()
    def move_card(self):
        if self.selected is True and pygame.mouse.get_pressed()[0] == True:
            self.position[0] = list(pygame.mouse.get_pos())[0] - 64
            self.position[1] = list(pygame.mouse.get_pos())[1] - 89




#basic attack card
basic_attack = card()
basic_attack.attack = 10
basic_attack.rarity = "common"
basic_attack.card_name = "Basic Attack"

basic_block = card()
basic_block.block = 5
basic_block.rarity = "common"
basic_block.card_name = "Basic Block"