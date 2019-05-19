
__copyright__ = "(c) Matthew Johnson 2019"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Matt"
__version__ = "2.0"

import pygame as p
import time
from random import shuffle

p.init()

from modules.board import *
from modules.write_words import *
from modules.variables import *

war_games_wave = p.mixer.Sound("asserts/That scene from War Games.wav")
gameDisplay = p.display.set_mode((width_display, height_display))
clock = p.time.Clock()

gameIco = p.image.load("asserts/tictactoe.png")
p.display.set_caption("Tic Tac Toe")
p.display.set_icon(gameIco)


def text_objects(text, font, colour):
    text_surf = font.render(str(text), True, colour)
    return text_surf, text_surf.get_rect()


def button(msg, colour, button_x, button_y, button_width, button_height, ic, ac, size, action=None):
    mouse = p.mouse.get_pos()
    click = p.mouse.get_pressed()

    if button_x + button_width > mouse[0] > button_x and button_y + button_height > mouse[1] > button_y:
        p.draw.rect(gameDisplay, ac, (button_x, button_y, button_width, button_height))
        if click[0] == 1 and action != None:
            action()
    else:
        p.draw.rect(gameDisplay, ic, (button_x, button_y, button_width, button_height))

    small_text = p.font.SysFont("comicsansms", size)
    text_surf, text_rect = text_objects(msg, small_text, colour)
    text_rect.center = ((button_x + (button_width/2)), (button_y + (button_height/2)))
    gameDisplay.blit(text_surf, text_rect)


def quit_game():
    p.quit()
    quit()


def game_intro():
    intro = True
    while intro:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()

        gameDisplay.fill(white)
        large_text = p.font.SysFont("comicsansms", 90)
        text_surf, text_rect = text_objects("Tic Tac Toe", large_text, black)
        text_rect.center = ((width_display/2), (height_display*(1/4)))
        gameDisplay.blit(text_surf, text_rect)

        button("START!", black, (width_display * (1/3)) - 100, height_display / 2, 150, 100, dark_green, green, 25, write_words)
        button("QUIT!", black, (width_display * (2/3)) - 50, height_display / 2, 150, 100, dark_red, red, 25, quit_game)

        clock.tick(15)
        p.display.update()


def unpause():
    time.sleep(.2)
    gameDisplay.fill(black)
    grid.set_up()


def paused():
    time.sleep(.5)
    gameDisplay.fill(black)
    pause = True
    while pause:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()
        large_text = p.font.SysFont("comicsansms", 90)
        text_surf, text_rect = text_objects("Paused", large_text, white)
        text_rect.center = ((width_display/2), (height_display*(1/4)))
        gameDisplay.blit(text_surf, text_rect)

        button("RESUME!", white, (width_display * (1/3)) - 100, height_display/2, 150, 100, dark_green, green, 25, unpause)
        button("QUIT!", white, (width_display * (2/3)) - 50, height_display/2, 150, 100, dark_red, red, 25, quit_game)

        clock.tick(15)
        p.display.update()


def game_loop():
    game_exit = False
    time.sleep(.2)
    while not game_exit:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_p:
                    paused()
            choose_piece()
        clock.tick(60)
        p.display.update()


game_intro()
p.quit()
quit()
