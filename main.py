import pygame
from os.path import join
import os
from text_box import *
from button_class import *


WIDTH, HEIGHT = 900, 750
FPS = 60
BG_COLOR = (0,0,0)
bg_list = []

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Login Page")

def load_dragon():
    dragon_idle = [pygame.image.load(join("assets", "Dragon", f"idle{i}.png")) for i in range(1,7)]
    dragon_run = [pygame.image.load(join("assets", "Dragon", f"run{i}.png")) for i in range(1,9)]

    
def draw_background():
    bg = pygame.image.load(join("assets", "Background.png"))
    screen.blit(bg, (0, -40))

def draw_login_page(input_boxes, rect, logo):
    screen.blit(rect, (WIDTH//2-150, HEIGHT//2-250))
    screen.blit(logo, (380, HEIGHT//2-195))

    for box in input_boxes:
            box.draw(screen, 10, 20)
    
    
def main():
    clock = pygame.time.Clock()
    input_box1 = InputBox(WIDTH//2-100, HEIGHT//2-20, 200, 45, email=True)
    input_box2 = InputBox(WIDTH//2-100, HEIGHT//2+60, 200, 45, password=True)
    input_boxes = [input_box1, input_box2]
    login_button = Button('Login', 200, 40, (WIDTH//2-100, 530), 5)

    rect = pygame.Surface((300,500))
    rect.set_alpha(230)
    rect.fill((255,255,255))

    logo = pygame.image.load(join("assets", "logo.png"))
    logo = pygame.transform.scale(logo, (140,140))

    dragon_idle = [pygame.image.load(join("assets", "Dragon", f"idle{i}.png")) for i in range(1,7)]
    dragon_idle = [pygame.transform.scale2x(i) for i in dragon_idle]
    dragon_run = [pygame.image.load(join("assets", "Dragon", f"run{i}.png")) for i in range(1,9)]
    dragon_run = [pygame.transform.scale2x(i) for i in dragon_run]
    dragon_fly_idle = [pygame.image.load(join("assets", "Dragon", f"fly_idle{i}.png")) for i in range(1,7)]
    dragon_fly_idle = [pygame.transform.scale2x(i) for i in dragon_fly_idle]
    dragon_fly = [pygame.image.load(join("assets", "Dragon", f"fly{i}.png")) for i in range(1,7)]
    dragon_fly = [pygame.transform.scale2x(i) for i in dragon_fly]
    dragon_attack = [pygame.image.load(join("assets", "Dragon", f"attack{i}.png")) for i in range(1,5)]
    dragon_attack = [pygame.transform.scale2x(i) for i in dragon_attack]
    count = 0
    variable = 36
    sprite_sheet = "fly"
    posx = -128
    posy = HEIGHT//2-32
    flipped = False

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)
        
        for box in input_boxes:
            box.update()

        screen.fill(BG_COLOR)

        draw_background()
        draw_login_page(input_boxes, rect, logo)
        
        login_button.draw(screen)
        login_button.check_click()
        
        
        if sprite_sheet in ["idle", "fly_idle", "fly"]: variable = 36
        if sprite_sheet == "run": variable = 48
        if sprite_sheet == "attack": variable = 16

        if count + 1 >= variable: 
            count = 0
        if sprite_sheet == "idle":
            if flipped != True: screen.blit(dragon_idle[count//6], (posx, posy))
            else:
                flipped_idle = [pygame.transform.flip(i, True, False) for i in dragon_idle]
                screen.blit(flipped_idle[count//6], (posx, posy))
        elif sprite_sheet == "run":
            if flipped != True: screen.blit(dragon_run[count//8], (posx, posy))  
            else:
                flipped_run = [pygame.transform.flip(i, True, False) for i in dragon_run]
                screen.blit(flipped_run[count//8], (posx, posy))
        elif sprite_sheet == "fly_idle":
            if flipped != True: screen.blit(dragon_fly_idle[count//6], (posx, posy))
            else:
                flipped_fly_idle = [pygame.transform.flip(i, True, False) for i in dragon_fly_idle]
                screen.blit(flipped_fly_idle[count//6], (posx, posy))
        elif sprite_sheet == "fly":
            if flipped != True: screen.blit(dragon_fly[count//6], (posx, posy))
            else:
                flipped_fly = [pygame.transform.flip(i, True, False) for i in dragon_fly]
                screen.blit(flipped_fly[count//6], (posx, posy))
            if posx < 90: posx += 2
            elif posx == 90: sprite_sheet = "fly_idle"
        elif sprite_sheet == "attack":
            if flipped != True: screen.blit(dragon_attack[count//4], (posx, posy))
            else:
                flipped_attack = [pygame.transform.flip(i, True, False) for i in dragon_attack]
                screen.blit(flipped_attack[count//6], (posx, posy))

        if input_box1.active:
            if posx <= 680:
                flipped = False
                sprite_sheet = "fly"
                posx += 3
            else:
                flipped = True
                sprite_sheet = "fly_idle"
        
        if input_box2.tick:
            if posx > 600:
                flipped = True
                sprite_sheet = "fly"
                posx -= 3
            elif posx <= 600:
                flipped = True
                sprite_sheet = "fly_idle"
            if posy <= 385:
                posy += 3
        elif input_box2.tick == False and input_box2.text != "":
            if posx <= 680:
                flipped = False
                sprite_sheet = "fly"
                posx += 3
            if posx > 600:
                sprite_sheet = "fly_idle"
        
            
        count += 1

    

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    main()