import sys, random, pygame

class enemy:
    health = 0
    attack = 0
    colour = (220, 20, 60)
    position = [800, 150]
    radius = 0
    def draw_enemy(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)
        #pygame.display.update

#gobline enemy :)
goblin = enemy()
goblin.health = 50
goblin.attack = 10
goblin.radius = 50