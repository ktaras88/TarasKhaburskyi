import pygame
from random import choice, randint

class Letter:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def move(self):
        ierog = ['α', 'β', 'γ', 'Δ', 'δ', 'ε', 'ζ', 'η', 'Θ', 'θ', 'ι','Λ', 'λ', 'μ', 'Ξ', 'ξ', 'ρ', 'Σ', 'ς','χ', 'Ψ', 'ψ', 'Ω', 'ω']       
        font = pygame.font.SysFont('Calibri', self.size, True, False)
        text = font.render(choice(ierog), True, (255, 255, 255))
        text1 = font.render(choice(ierog), True, (randint(0, 50), randint(100, 200), randint(50, 100)))
        text2 = font.render(choice(ierog), True, (randint(0, 50), randint(100, 200), randint(50, 100)))
        text3 = font.render(choice(ierog), True, (randint(0, 50), randint(100, 200), randint(50, 100)))
        text4 = font.render(choice(ierog), True, (randint(0, 50), randint(100, 200), randint(50, 100)))

        if self.y < display_hight:
            screen.blit(text, [self.x, self.y])
            screen.blit(text1, [self.x, self.y-self.size])
            screen.blit(text2, [self.x, self.y-2*self.size])
            screen.blit(text3, [self.x, self.y-3*self.size])
            screen.blit(text4, [self.x, self.y-4*self.size])
            self.y += self.size
            
        else:
            self.x = randint(0,display_width)
            self.y = randint(0, display_hight)
            self.size = randint(3,15)
           
def create_letter_arr(array):
    array.append(Letter(100, display_hight-5, 15))
    array.append(Letter(200, display_hight-5, 20))
    array.append(Letter(300, display_hight-5, 16))
    array.append(Letter(400, display_hight-5, 15))
    array.append(Letter(500, display_hight-5, 12))

def draw_array(array):
    for letter in array:
        letter.move()

#-------------------main-----------------------

pygame.init()
display_width = 700
display_hight = 500
screen = pygame.display.set_mode((display_width,display_hight))
pygame.display.set_caption("MATRIX")
clock = pygame.time.Clock()

letter_arr = []

run = True
while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    screen.fill((0, 0, 0))
    create_letter_arr(letter_arr)
    draw_array(letter_arr)

    pygame.display.update()
    clock.tick(10)