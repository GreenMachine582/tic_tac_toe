import pygame as p
import time

grey = (150, 150, 150)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (250, 250, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (200, 0, 150)
dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
dark_blue = (0, 0, 200)
dark_pink = (150, 0, 200)

width_display = 800
height_display = 600
num_squares = 3
side_square = 173
border = 20

p_piece = None
ai_piece = None
game_piece = None
h = True

x_test = ""
y_test = ""
square_place = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
turn_count = 1
draw_count = 0
win_count = 0
lose_count = 0

square_0 = [20, 20, "", grey, green, 0]
square_1 = [213, 20, "", grey, green, 1]
square_2 = [406, 20, "", grey, green, 2]
square_3 = [20, 213, "", grey, green, 3]
square_4 = [213, 213, "", grey, green, 4]
square_5 = [406, 213, "", grey, green, 5]
square_6 = [20, 406, "", grey, green, 6]
square_7 = [213, 406, "", grey, green, 7]
square_8 = [406, 406, "", grey, green, 8]

square_array = [square_0, square_1, square_2, square_3, square_4, square_5, square_6, square_7, square_8]

war_games_wave = p.mixer.Sound("asserts/That scene from War Games.wav")
gameDisplay = p.display.set_mode((width_display, height_display))
clock = p.time.Clock()

gameIco = p.image.load("asserts/tictactoe.png")
p.display.set_caption("Tic Tac Toe")
p.display.set_icon(gameIco)
