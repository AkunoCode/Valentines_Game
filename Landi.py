import sys
import time
import pygame
import os
from random import randint

pygame.init()

#ELEMENTS:
dimension_x, dimension_y = 600, 600
screen = pygame.display.set_mode((dimension_x,dimension_y))
pygame.display.set_caption("Will You Be My Date?")

pygame.display.set_icon(pygame.image.load(os.path.abspath('Images/icon.png')))

font_small = pygame.font.Font(os.path.abspath('Images/Pixel.ttf'), 25)

#Buttons
button_width = 100
button_height = 50
yes_button_x, yes_button_y = 175, 475
no_button_x, no_button_y = 325, 475

# Create the buttons
yes_button = pygame.Rect(yes_button_x, yes_button_y, button_width, button_height)
no_button = pygame.Rect(no_button_x, no_button_y, button_width, button_height)
button_color = (255, 255, 255)

# Button labels
yes_label = font_small.render("Yes", True, (229, 115, 115))
no_label = font_small.render("No", True, (229, 115, 115))

# Images:
background = pygame.image.load(os.path.abspath('Images/Background.jpg'))
background = pygame.transform.scale(background,(dimension_x,dimension_y))
display_imgs = []

#ImageBG
imageBG = pygame.Rect(50,50,500,400)

for i in os.listdir('Images/Display'):
    if i in ['yes.jpg','yes.png']:
        yes = ''.join('Images/Display/'+i)
    elif (i.endswith('.jpg') or i.endswith('.png')):
        display_imgs.append(os.path.abspath(''.join('Images/Display/'+i)))

display_imgs = [pygame.image.load(i) for i in display_imgs]
display_imgs = [pygame.transform.scale(i,(250,250)) for i in display_imgs]
yes_img = pygame.image.load(os.path.abspath(yes))
yes_img = pygame.transform.scale(yes_img,(250,250))
num_img = len(display_imgs) - 1




def main_game():
    running = True
    change_display = display_imgs[0]
    please = ["Pleaseee??","Why no???", "???", "Maybe we can try??", "Please be my valentines","Did you mean yes??"]
    date = font_small.render("Hi, crushie! Can you be my valentines?",True,(229, 115, 115))
    text_size = date.get_size()
    wait = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                change_display = display_imgs[randint(0,num_img)]
                date = font_small.render("Wait! Don't leave me yet.",True,(229, 115, 115))
                text_size = date.get_size()
        
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if yes_button.collidepoint(mouse_x, mouse_y):
                    change_display = yes_img
                    date = font_small.render("Really?! Thank youu~",True,(229, 115, 115))
                    text_size = date.get_size()
                    wait = True
                elif no_button.collidepoint(mouse_x, mouse_y):
                    change_display = display_imgs[randint(0,num_img)]
                    date = font_small.render(please[randint(0,len(please)-1)],True,(229, 115, 115))
                    text_size = date.get_size()


        screen.blit(background,(0,0))

        pygame.draw.rect(screen,button_color,imageBG)
        pygame.draw.rect(screen,(229, 115, 115),imageBG,3)
        screen.blit(change_display,(175,100))
        screen.blit(date,(imageBG.centerx - text_size[0] // 2, 375))
        
        # Draw the buttons
        pygame.draw.rect(screen, button_color, yes_button)
        pygame.draw.rect(screen, button_color, no_button)
        pygame.draw.rect(screen, (229, 115, 115), yes_button,3)
        pygame.draw.rect(screen, (229, 115, 115), no_button,3)

        screen.blit(yes_label, (yes_button_x + button_width // 2 - yes_label.get_width() // 2, yes_button_y + button_height // 2 - yes_label.get_height() // 2))
        screen.blit(no_label, (no_button_x + button_width // 2 - no_label.get_width() // 2, no_button_y + button_height // 2 - no_label.get_height() // 2))
    

        pygame.display.update()
        if wait:
            time.sleep(1)
            running = False
            sys.exit()

if __name__ == '__main__':
    main_game()