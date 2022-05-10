import pygame_menu

import constants
import pygame


class DisplayComponent:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((constants.window_width, constants.window_height))
        pygame.display.set_caption("Tic Tac Toe - Projekt SI - 184916 184306 184657")

        # Menu setup
        self._menu = pygame_menu.Menu("Tic Tac Toe", constants.window_width, constants.window_height,
                                      theme=pygame_menu.themes.THEME_DARK)
        self._menu.add.selector('Difficulty :', [('Normal_AI', constants.ai_easy), ('Medium_AI', constants.ai_medium),
                                                 ('Hard_AI', constants.ai_hard)],
                                onchange=self.set_menu_difficulty_chosen)
        self._menu.add.button('Play', self.set_menu_play_chosen)
        self._menu.add.button('Instructions', self.set_menu_instruction_chosen)
        self._menu.add.button('Quit', self.set_menu_exit_chosen)
        self._menu_action_chosen = None
        self._menu_difficulty_chosen = constants.ai_easy

        self._x_sign = pygame.transform.scale(pygame.image.load("x_sign.png"),
                                              (constants.pile_width, constants.pile_height))
        self._o_sign = pygame.transform.scale(pygame.image.load("o_sign.jpg"),
                                              (constants.pile_width, constants.pile_height))
        self._empty_sign = pygame.transform.scale(pygame.image.load("empty_sign.png"),
                                              (constants.pile_width, constants.pile_height))

    def use_menu(self):
        self.set_menu_difficulty_chosen(None, constants.ai_easy)
        self._menu.enable()
        self._menu.mainloop(self._screen)
        return self._menu_action_chosen, self._menu_difficulty_chosen

    def set_menu_play_chosen(self):
        self._menu_action_chosen = constants.menu_play_game
        self._menu.disable()

    def set_menu_exit_chosen(self):
        self._menu_action_chosen = constants.menu_exit
        self._menu.disable()

    def set_menu_instruction_chosen(self):
        self._menu_action_chosen = constants.menu_instruction
        self._menu.disable()

    def set_menu_difficulty_chosen(self, _, difficulty):
        self._menu_difficulty_chosen = difficulty

    def display_result(self, winner):
        print(f"Wins: {winner}")
        print("Wanna play again?")

    def display_board(self, board):
        self._screen.fill(constants.white_color)
        for i in range(board.size):
            for j in range(board.size):
                self._screen.blit(self._x_sign if board[i][j] == 'x' else (self._o_sign if board[i][j] == 'o' else self._empty_sign),
                                  (i * constants.pile_width, j * constants.pile_height))
        pygame.display.update()
        pygame.display.flip()

    def display_instruction(self):
        print("!!!!!!!! Quick tutorial just to let you in!")
        print("You are playing as 'x'. AI plays as 'o'")
        print("123")
        print("456")
        print("789")
        print("Positioning is left-upper corner based. 1 is located (0, 0)")
        print("8 is located (2, 1) etc.")

    def get_events(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                return constants.menu_exit, None, None
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                return constants.mouse_clicked, int(pos[0]/constants.pile_width), int(pos[1]/constants.pile_height)
        return None, None, None

    def __del__(self):
        pygame.quit()