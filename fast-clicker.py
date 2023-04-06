import pygame 
import random
pygame.init()

window = pygame.display.set_mode(500,500)
window.fill((153, 163, 173))

clock = pygame.time.Clock()

class Area():
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def set_color(self, new_color): 
        self.color = new_color

    def fill(self):
        pygame.draw.rect(window, self.color, self.rect)

    
        
class Label(Area):
    def set_text(self, text, tsize, color=(0,0,0)):
        font = pygame.font.Font('Forte', tsize)
        self.text = ""
        self.text = font.render(text, True, color)


    def draw(self, dx=0, dy=0):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, (self.rect.x+dx, self.rect.y+dy))

cards = []
num_cards = 4 
x = 70 
for i in range(num_cards): 
    new_card = Label(x, 170, 70, 100, (255, 255, 255))
    new_card.set_text('Click', 30)
    cards.append(new_card)
    x += 100

timer_text = Label(0, 0, 50, 50, (0,0,0,0))
timer_text.set_text('Час:', 40)
timer_text.draw(20, 20)

timer_count = Label(50, 55, 50, 50, (0,0,0,0))
timer_count.set_text('0', 40)
timer_count.draw(0, 0)

score_text = Label(380, 0, 50, 50, (0,0,0,0))
score_text.set_text('Рахунок:', 40)
score_text.draw(20, 20)

score_count = Label(430, 55, 50, 50, (0,0,0,0))
score_count.set_text('0', 40)
score_count.draw(0, 0)

score = 0
import time 
start_time = time.time()
cur_time = start_time
wait = 0

game = True 

while game:
    new_time = time.time()
    if new_time-cur_time >= 1: 
        timer_count.set_text(str(new_time), 40)
        timer_count.draw()
        cur_time = new_time
        pygame.display.update
    if wait == 0:
        number = random.randint(0,3)
        for i in range (num_cards):
            cards[i].set_color((255, 255, 255))
            cards[i].fill()
            if number == i:
                cards[i].draw(14, 38)
        wait = 20
    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].rect.collidepoint(x, y):
                    if number == i:
                        cards[i].set_color((0, 200 ,0))
                        score += 1 
                    else:
                        cards[i].set_color((200 ,0 ,0))                        
                        score -= 1

                    cards[i].fill()
                    score_count.set_text(str(score), 40)
                    score_count.draw(0 ,0)
                    pygame.display.update()

    clock.tick(40)
    pygame.display.update()
