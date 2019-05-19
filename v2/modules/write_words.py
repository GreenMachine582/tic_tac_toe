
import pygame as p

from modules.variables import *
from modules.board import *
import __main__


def write_words():
    gameDisplay.fill(white)
    name = []
    question = str('Please enter your name:')
    write = True
    while write:
        large_text = p.font.SysFont("comicsansms", 60)
        small_text = p.font.SysFont("comicsansms", 50)
        text_surf, text_rect = __main__.text_objects(question, large_text, black)
        text_rect.center = ((width_display / 2), (height_display * (1 / 3)))
        gameDisplay.blit(text_surf, text_rect)
        
        for event in p.event.get():
            if event.type == p.QUIT:
                __main__.quit_game()
            if event.type == p.KEYDOWN:
                letter = ''
                if event.key == p.K_RETURN:
                    __main__.game_loop()
                elif event.key == p.K_BACKSPACE:
                    nameS = name
                    nameS = list(nameS)
                    del nameS[-1]
                    nameS = "".join(nameS)
                    name = nameS
                elif event.key == p.K_SPACE:
                    letter = ' '
                elif event.key == p.K_a:
                    letter = 'a'
                elif event.key == p.K_b:
                    letter = 'b'
                elif event.key == p.K_c:
                    letter = 'c'
                elif event.key == p.K_d:
                    letter = 'd'
                elif event.key == p.K_e:
                    letter = 'e'
                elif event.key == p.K_f:
                    letter = 'f'
                elif event.key == p.K_g:
                    letter = 'g'
                elif event.key == p.K_h:
                    letter = 'h'
                elif event.key == p.K_i:
                    letter = 'i'
                elif event.key == p.K_j:
                    letter = 'j'
                elif event.key == p.K_k:
                    letter = 'k'
                elif event.key == p.K_l:
                    letter = 'l'
                elif event.key == p.K_m:
                    letter = 'm'
                elif event.key == p.K_n:
                    letter = 'n'
                elif event.key == p.K_o:
                    letter = 'o'
                elif event.key == p.K_p:
                    letter = 'p'
                elif event.key == p.K_q:
                    letter = 'q'
                elif event.key == p.K_r:
                    letter = 'r'
                elif event.key == p.K_s:
                    letter = 's'
                elif event.key == p.K_t:
                    letter = 't'
                elif event.key == p.K_u:
                    letter = 'u'
                elif event.key == p.K_v:
                    letter = 'v'
                elif event.key == p.K_w:
                    letter = 'w'
                elif event.key == p.K_x:
                    letter = 'x'
                elif event.key == p.K_y:
                    letter = 'y'
                elif event.key == p.K_z:
                    letter = 'z'
                name = ''.join(name)
                name = str(name) + str(letter)

            gameDisplay.fill(white)
            text_surf, text_rect = __main__.text_objects(question, large_text, black)
            text_rect.center = ((width_display / 2), (height_display * (1 / 3)))
            gameDisplay.blit(text_surf, text_rect)
            
            text_surf, text_rect = __main__.text_objects(name, small_text, black)
            text_rect.center = ((width_display / 2), (height_display * (1 / 2)))
            gameDisplay.blit(text_surf, text_rect)


        clock.tick(15)
        p.display.update()
