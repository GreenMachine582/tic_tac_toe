
import pygame as p
import time
from random import shuffle


from modules.variables import *
import __main__
    

def choose_piece():
    time.sleep(.2)
    choose = True
    while choose:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                quit()

        gameDisplay.fill(white)
        large_text = p.font.SysFont("comicsansms", 90)
        text_surf, text_rect = __main__.text_objects("Which Team", large_text, black)
        text_rect.center = ((width_display / 2), (height_display * (1 / 4)))
        gameDisplay.blit(text_surf, text_rect)
        __main__.button("X", black, (width_display * (1/3)) - 100, height_display / 2, 150, 100, dark_blue, blue, 45, grid.set_x)
        __main__.button("O", black, (width_display * (2/3)) - 50, height_display / 2, 150, 100, dark_pink, pink, 45, grid.set_o)

        clock.tick(15)
        p.display.update()


class Grid:

    def __init__(self):
        self.side_square = side_square - border
        self.colour = black
        self.p_piece = p_piece
        self.ai_piece = ai_piece
        self.game_piece = game_piece
        self.turn_count = turn_count
        self.draw_count = draw_count
        self.win_count = win_count
        self.lose_count = lose_count
        self.square_place = square_place
        self.c = 0

    def set_up(self):
        __main__.button("", black, 600, 20, 180, 560, black, black, 25, None)
        win1 = [("Win:"), 80]
        win2 = [(str(self.win_count)), 160]
        draw1 = [("Draw:"), 240]
        draw2 = [(str(self.draw_count)), 320]
        lose1 = [("Lose:"), 400]
        lose2 = [(str(self.lose_count)), 480]
        for i in [win1, win2, draw1, draw2, lose1, lose2]:
            x = 680
            y = i[1]
            i.pop(1)
            i = ''.join(i)
            large_text = p.font.SysFont("comicsansms", 50)
            text_surf, text_rect = __main__.text_objects(i, large_text, white)
            text_rect.center = (x, y)
            gameDisplay.blit(text_surf, text_rect)
        p.display.update()
        self.button_grid()

    def button_grid(self):
        global h, x_test, y_test
        draw = True
        while draw:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    quit()
                elif event.type == p.KEYDOWN:
                    if event.key == p.K_p:
                        __main__.paused()

            for i in square_array:
                x = i[0]
                y = i[1]
                game_piece = i[2]
                ic = i[3]
                ac = i[4]

                x_test = x
                y_test = y
                mouse = p.mouse.get_pos()
                click = p.mouse.get_pressed()

                small_text = p.font.SysFont("comicsansms", 150)
                text_surf, text_rect = __main__.text_objects(game_piece, small_text, self.colour)
                text_rect.center = ((x + (self.side_square / 1.75)), (y + (self.side_square / 1.75)))

                if x + side_square > mouse[0] > x and y + side_square > mouse[1] > y:
                    p.draw.rect(gameDisplay, ac, (x, y, side_square, side_square))
                    if click[0] == 1:
                        time.sleep(.2)
                        for i in square_array:
                            square_x = i[0]
                            square_y = i[1]
                            piece_type = i[2]
                            place = i[5]
                            if square_x == x and square_y == y:
                                if game_piece == "X" or game_piece == "O":
                                    self.turn_count -= 1
                                    h = False
                                    self.piece_checker()
                                else:
                                    h = True
                                    square_array.remove(i)
                                    i.pop(2)
                                    i.pop(2)
                                    i.pop(2)
                                    i.insert(2, self.p_piece)
                                    i.insert(3, green)
                                    i.insert(4, green)
                                    square_array.insert(place, i)
                                    self.coded_board()
                        text_surf, text_rect = text_objects(game_piece, small_text, self.colour)
                        gameDisplay.blit(text_surf, text_rect)
                else:
                    p.draw.rect(gameDisplay, ic, (x, y, side_square, side_square))

                gameDisplay.blit(text_surf, text_rect)
            clock.tick(60)
            p.display.update()

    def reset(self):
        global square_array
        self.square_place = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        s_0 = [20, 20, "", grey, green, 0]
        s_1 = [213, 20, "", grey, green, 1]
        s_2 = [406, 20, "", grey, green, 2]
        s_3 = [20, 213, "", grey, green, 3]
        s_4 = [213, 213, "", grey, green, 4]
        s_5 = [406, 213, "", grey, green, 5]
        s_6 = [20, 406, "", grey, green, 6]
        s_7 = [213, 406, "", grey, green, 7]
        s_8 = [406, 406, "", grey, green, 8]
        square_array = [s_0, s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8]
        self.turn_count = 1
        self.c = 0
        __main__.game_loop()

    def winner(self):
        time.sleep(.5)
        gameDisplay.fill(black)
        self.win_count += 1
        choose = True
        while choose:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    quit()

            large_text = p.font.SysFont("comicsansms", 60)
            text_surf, text_rect = __main__.text_objects("You are the Winner!", large_text, white)
            text_rect.center = ((width_display / 2), (height_display * (1 / 4)))
            gameDisplay.blit(text_surf, text_rect)
            __main__.button("REMATCH!", white, (width_display * (1/3)) - 100, height_display / 2, 150, 100, dark_green, green,
                   25, self.reset)
            __main__.button("QUIT!", white, (width_display * (2/3)) - 50, height_display / 2, 150, 100, dark_red, red,
                   25, __main__.quit_game)

            clock.tick(15)
            p.display.update()

    def loser(self):
        time.sleep(.5)
        gameDisplay.fill(black)
        self.lose_count += 1
        choose = True
        while choose:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    quit()

            large_text = p.font.SysFont("comicsansms", 60)
            text_surf, text_rect = __main__.text_objects("AI is the Winner!", large_text, white)
            text_rect.center = ((width_display / 2), (height_display * (1 / 4)))
            gameDisplay.blit(text_surf, text_rect)
            __main__.button("REMATCH!", white, (width_display - 100) * (1 / 4), height_display / 2, 150, 100, dark_green, green,
                   25, self.reset)
            __main__.button("QUIT!", white, (width_display - 100) * (3 / 4), height_display / 2, 150, 100, dark_red, red,
                   25, __main__.quit_game)

            clock.tick(15)
            p.display.update()

    def draw(self):
        time.sleep(.5)
        gameDisplay.fill(black)
        choose = True
        self.draw_count += 1
        if self.draw_count == 5:
            self.war_games()
        else:
            while choose:
                for event in p.event.get():
                    if event.type == p.QUIT:
                        p.quit()
                        quit()

                large_text = p.font.SysFont("comicsansms", 50)
                text_surf, text_rect = __main__.text_objects("The Game was a Draw", large_text, white)
                text_rect.center = ((width_display / 2), (height_display * (1 / 4)))
                gameDisplay.blit(text_surf, text_rect)
                __main__.button("REMATCH!", white, (width_display * (1/3)) - 100, height_display / 2, 150, 100, dark_green, green,
                       25, self.reset)
                __main__.button("QUIT!", white, (width_display * (2/3)) - 50, height_display / 2, 150, 100, dark_red, red,
                       25, __main__.quit_game)

                clock.tick(15)
                p.display.update()

    def war_games(self):
        gameDisplay.fill(black)
        p.mixer.Sound.play(war_games_wave)
        y_base = 5
        quote = ["A STRANGE GAME.", "THE ONLY WINNING MOVE", "IS NOT TO PLAY."]
        words_music = True
        while words_music:
            for line in quote:
                y_base += 1
                y = 50 * y_base
                x_base = 0
                for letter in line:
                    x_base += 1
                    x = 15 * x_base
                    large_text = p.font.SysFont("vgasys", 20)
                    text_surf, text_rect = __main__.text_objects(letter, large_text, white)
                    text_rect = (x, y)
                    gameDisplay.blit(text_surf, text_rect)
                    clock.tick(10)
                    p.display.update()
            words_music = False
        time.sleep(.2)
        __main__.quit_game()

    def coded_board(self):
        global x_test, y_test, square_array
        for i in square_array:
            x_t = i[0]
            y_t = i[1]
            piece_type = i[2]
            place = i[5]
            if x_t == x_test and y_t == y_test:
                if piece_type == "X":
                    self.square_place.pop(place)
                    self.square_place.insert(place, "X")
                elif piece_type == "O":
                    self.square_place.pop(place)
                    self.square_place.insert(place, "O")
        self.update_grid()

    def update_grid(self):
        for i in square_array:
            x = i[0]
            y = i[1]
            game_piece = i[2]
            ic = i[3]
            ac = i[4]

            small_text = p.font.SysFont("comicsansms", 150)
            text_surf, text_rect = __main__.text_objects(game_piece, small_text, self.colour)
            text_rect.center = ((x + (self.side_square / 1.75)), (y + (self.side_square / 1.75)))

            p.draw.rect(gameDisplay, ic, (x, y, side_square, side_square))

            gameDisplay.blit(text_surf, text_rect)
        clock.tick(60)
        p.display.update()
        self.piece_checker()

    def piece_checker(self):
        global h
        
        if self.square_place[0] == self.square_place[1] and self.square_place[0] == self.square_place[2]:
            if self.p_piece == self.square_place[0]:
                self.winner()
            else:
                self.loser()
        elif self.square_place[3] == self.square_place[4] and self.square_place[3] == self.square_place[5]:
            if self.p_piece == self.square_place[3]:
                self.winner()
            else:
                self.loser()
        elif self.square_place[6] == self.square_place[7] and self.square_place[6] == self.square_place[8]:
            if self.p_piece == self.square_place[6]:
                self.winner()
            else:
                self.loser()
        elif self.square_place[0] == self.square_place[3] and self.square_place[0] == self.square_place[6]:
            if self.p_piece == self.square_place[0]:
                self.winner()
            else:
                self.loser()
        elif self.square_place[1] == self.square_place[4] and self.square_place[1] == self.square_place[7]:
            if self.p_piece == self.square_place[1]:
                self.winner()
            else:
                self.loser()
        elif self.square_place[2] == self.square_place[5] and self.square_place[2] == self.square_place[8]:
            if self.p_piece == self.square_place[2]:
                self.winner()
            else:
                self.loser()
        elif self.square_place[0] == self.square_place[4] and self.square_place[0] == self.square_place[8]:
            if self.p_piece == self.square_place[0]:
                self.winner()
            else:
                self.loser()
        elif self.square_place[2] == self.square_place[4] and self.square_place[2] == self.square_place[6]:
            if self.p_piece == self.square_place[2]:
                self.winner()
            else:
                self.loser()

        if h:
            self.c += 1
            if self.turn_count == 9:
                self.draw()
            self.turn_count += 1
            if self.c == 2:
                self.c = 0
                self.piece()
            else:
                self.computer_winning_move()
        self.piece()

    def computer_winning_move(self):
        best_moves = []
        
##        rows
        if self.square_place[0] != '0' and self.square_place[1] != '1' and self.square_place[2] != '2':
            None
        else:
            if self.square_place[0] == self.square_place[1] and self.square_place[0] == self.ai_piece:
                best_moves.insert(0, 2)
            elif self.square_place[1] == self.square_place[2] and self.square_place[1] == self.ai_piece:
                best_moves.insert(0, 0)
            elif self.square_place[0] == self.square_place[2] and self.square_place[0] == self.ai_piece:
                best_moves.insert(0, 1)

        if self.square_place[3] != '3' and self.square_place[4] != '4' and self.square_place[5] != '5':
            None
        else:
            if self.square_place[3] == self.square_place[4] and self.square_place[3] == self.ai_piece:
                best_moves.insert(0, 5)
            elif self.square_place[4] == self.square_place[5] and self.square_place[4] == self.ai_piece:
                best_moves.insert(0, 3)
            elif self.square_place[3] == self.square_place[5] and self.square_place[3] == self.ai_piece:
                best_moves.insert(0, 4)

        if self.square_place[6] != '6' and self.square_place[7] != '7' and self.square_place[8] != '8':
            None
        else:
            if self.square_place[6] == self.square_place[7] and self.square_place[6] == self.ai_piece:
                best_moves.insert(0, 8)
            elif self.square_place[7] == self.square_place[8] and self.square_place[7] == self.ai_piece:
                best_moves.insert(0, 6)
            elif self.square_place[6] == self.square_place[8] and self.square_place[6] == self.ai_piece:
                best_moves.insert(0, 7)
##        rows

##        coloums
        if self.square_place[0] != '0' and self.square_place[3] != '3' and self.square_place[6] != '6':
            None
        else:
            if self.square_place[0] == self.square_place[3] and self.square_place[0] == self.ai_piece:
                best_moves.insert(0, 6)
            elif self.square_place[3] == self.square_place[6] and self.square_place[3] == self.ai_piece:
                best_moves.insert(0, 0)
            elif self.square_place[0] == self.square_place[6] and self.square_place[0] == self.ai_piece:
                best_moves.insert(0, 3)
                
        if self.square_place[1] != '1' and self.square_place[4] != '4' and self.square_place[7] != '7':
            None
        else: 
            if self.square_place[1] == self.square_place[4] and self.square_place[1] == self.ai_piece:
                best_moves.insert(0, 7)
            elif self.square_place[4] == self.square_place[7] and self.square_place[4] == self.ai_piece:
                best_moves.insert(0, 1)
            elif self.square_place[1] == self.square_place[7] and self.square_place[1] == self.ai_piece:
                best_moves.insert(0, 4)
        if self.square_place[2] != '2' and self.square_place[5] != '5' and self.square_place[8] != '8':
            None
        else:
            if self.square_place[2] == self.square_place[5] and self.square_place[2] == self.ai_piece:
                best_moves.insert(0, 8)
            elif self.square_place[5] == self.square_place[8] and self.square_place[5] == self.ai_piece:
                best_moves.insert(0, 2)
            elif self.square_place[2] == self.square_place[8] and self.square_place[2] == self.ai_piece:
                best_moves.insert(0, 5)
##        coloums

##        diagonals
        if self.square_place[0] != '0' and self.square_place[4] != '4' and self.square_place[8] != '8':
            None
        else:
            if self.square_place[0] == self.square_place[4] and self.square_place[0] == self.ai_piece:
                best_moves.insert(0, 8)
            elif self.square_place[4] == self.square_place[8] and self.square_place[4] == self.ai_piece:
                best_moves.insert(0, 0)
            elif self.square_place[0] == self.square_place[8] and self.square_place[0] == self.ai_piece:
                best_moves.insert(0, 4)

        if self.square_place[2] != '2' and self.square_place[4] != '4' and self.square_place[6] != '6':
            None
        else:
            if self.square_place[2] == self.square_place[4] and self.square_place[2] == self.ai_piece:
                best_moves.insert(0, 6)
            elif self.square_place[4] == self.square_place[6] and self.square_place[4] == self.ai_piece:
                best_moves.insert(0, 2)
            elif self.square_place[2] == self.square_place[6] and self.square_place[2] == self.ai_piece:
                best_moves.insert(0, 4)
##        diagonals
        
        if best_moves != []:
            self.computer_move(best_moves)
        else:
            self.computer_counter_move()

    def computer_counter_move(self):
        best_moves = []
##        rows
        if self.square_place[0] != '0' and self.square_place[1] != '1' and self.square_place[2] != '2':
            None
        else:
            if self.square_place[0] == self.square_place[1] and self.square_place[0] == self.p_piece:
                best_moves.insert(0, 2)
            elif self.square_place[1] == self.square_place[2] and self.square_place[1] == self.p_piece:
                best_moves.insert(0, 0)
            elif self.square_place[0] == self.square_place[2] and self.square_place[0] == self.p_piece:
                best_moves.insert(0, 1)

        if self.square_place[3] != '3' and self.square_place[4] != '4' and self.square_place[5] != '5':
            None
        else:
            if self.square_place[3] == self.square_place[4] and self.square_place[3] == self.p_piece:
                best_moves.insert(0, 5)
            elif self.square_place[4] == self.square_place[5] and self.square_place[4] == self.p_piece:
                best_moves.insert(0, 3)
            elif self.square_place[3] == self.square_place[5] and self.square_place[3] == self.p_piece:
                best_moves.insert(0, 4)

        if self.square_place[6] != '6' and self.square_place[7] != '7' and self.square_place[8] != '8':
            None
        else:
            if self.square_place[6] == self.square_place[7] and self.square_place[6] == self.p_piece:
                best_moves.insert(0, 8)
            elif self.square_place[7] == self.square_place[8] and self.square_place[7] == self.p_piece:
                best_moves.insert(0, 6)
            elif self.square_place[6] == self.square_place[8] and self.square_place[6] == self.p_piece:
                best_moves.insert(0, 7)
##        rows

##        coloums
        if self.square_place[0] != '0' and self.square_place[3] != '3' and self.square_place[6] != '6':
            None
        else:
            if self.square_place[0] == self.square_place[3] and self.square_place[0] == self.p_piece:
                best_moves.insert(0, 6)
            elif self.square_place[3] == self.square_place[6] and self.square_place[3] == self.p_piece:
                best_moves.insert(0, 0)
            elif self.square_place[0] == self.square_place[6] and self.square_place[0] == self.p_piece:
                best_moves.insert(0, 3)
                
        if self.square_place[1] != '1' and self.square_place[4] != '4' and self.square_place[7] != '7':
            None
        else: 
            if self.square_place[1] == self.square_place[4] and self.square_place[1] == self.p_piece:
                best_moves.insert(0, 7)
            elif self.square_place[4] == self.square_place[7] and self.square_place[4] == self.p_piece:
                best_moves.insert(0, 1)
            elif self.square_place[1] == self.square_place[7] and self.square_place[1] == self.p_piece:
                best_moves.insert(0, 4)
        if self.square_place[2] != '2' and self.square_place[5] != '5' and self.square_place[8] != '8':
            None
        else:
            if self.square_place[2] == self.square_place[5] and self.square_place[2] == self.p_piece:
                best_moves.insert(0, 8)
            elif self.square_place[5] == self.square_place[8] and self.square_place[5] == self.p_piece:
                best_moves.insert(0, 2)
            elif self.square_place[2] == self.square_place[8] and self.square_place[2] == self.p_piece:
                best_moves.insert(0, 5)
##        coloums

##        diagonals
        if self.square_place[0] != '0' and self.square_place[4] != '4' and self.square_place[8] != '8':
            None
        else:
            if self.square_place[0] == self.square_place[4] and self.square_place[0] == self.p_piece:
                best_moves.insert(0, 8)
            elif self.square_place[4] == self.square_place[8] and self.square_place[4] == self.p_piece:
                best_moves.insert(0, 0)
            elif self.square_place[0] == self.square_place[8] and self.square_place[0] == self.p_piece:
                best_moves.insert(0, 4)

        if self.square_place[2] != '2' and self.square_place[4] != '4' and self.square_place[6] != '6':
            None
        else:
            if self.square_place[2] == self.square_place[4] and self.square_place[2] == self.p_piece:
                best_moves.insert(0, 6)
            elif self.square_place[4] == self.square_place[6] and self.square_place[4] == self.p_piece:
                best_moves.insert(0, 2)
            elif self.square_place[2] == self.square_place[6] and self.square_place[2] == self.p_piece:
                best_moves.insert(0, 4)
##        diagonals

        if best_moves != []:
            self.computer_move(best_moves)
        else:
            best_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]
            shuffle(best_moves)
            self.computer_move(best_moves)

    def computer_move(self, best_moves):
        global x_test, y_test, square_array
        legal_moves = []
        for i in best_moves:
            m = self.square_place[i]
            if m != "X" and m != "O":
                legal_moves.append(i)
        if legal_moves == []:
            self.piece_checker()
            
        move = legal_moves[0]
        if self.ai_piece == "X":
            self.square_place.pop(move)
            self.square_place.insert(move, "X")
        elif self.ai_piece == "O":
            self.square_place.pop(move)
            self.square_place.insert(move, "O")
        
        i = legal_moves[0]
        p = square_array[int(i)]
        p.pop(2)
        p.pop(2)
        p.insert(2, self.ai_piece)
        p.insert(3, green)
        square_array[i] = p
        self.update_grid()

    def piece(self):
        global h
        if h:
            if self.game_piece == self.p_piece:
                self.game_piece = self.ai_piece
            elif self.game_piece == self.ai_piece:
                self.game_piece = self.p_piece
        self.set_up()

    def set_x(self):
        time.sleep(.2)
        self.p_piece = "X"
        self.ai_piece = "O"
        self.game_piece = "X"
        gameDisplay.fill(black)
        grid.set_up()

    def set_o(self):
        time.sleep(.2)
        self.p_piece = "O"
        self.ai_piece = "X"
        self.game_piece = "O"
        gameDisplay.fill(black)
        grid.set_up()

grid = Grid()
