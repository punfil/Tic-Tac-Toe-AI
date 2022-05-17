import pygame_menu

import constants
import pygame


# todo this should have access to game or board, to get dimensions (w, h) and stuff
class DisplayComponent:
    def __init__(self, game):
        self._game = game

        pygame.init()
        self._screen = pygame.display.set_mode((constants.window_width, constants.window_height))
        pygame.display.set_caption("Tic Tac Toe - Projekt SI - 184916 184306 184657")

        # Menu setup
        self._menu = pygame_menu.Menu("Tic Tac Toe", constants.window_width, constants.window_height,
                                      theme=pygame_menu.themes.THEME_DARK)
        ###self._menu.add.selector('Difficulty :', [('MinMax AI', constants.ai_easy),
        ###                                         ('AlphaBeta AI', constants.ai_medium),
        ###                                         ('Neural AI', constants.ai_hard)],
        ###                        onchange=self.set_menu_difficulty_chosen)
        self._menu.add.button('Play', self.set_menu_play_chosen)
        self._menu.add.button('Quit', self.set_menu_exit_chosen)
        self._menu_action_chosen = None
        ###self._menu_difficulty_chosen = constants.ai_easy

        self._tile_width = constants.window_width / constants.board_width
        self._tile_height = constants.window_height / constants.board_height
        self._x_symbol = pygame.transform.scale(pygame.image.load("x_sign.png"), (self._tile_width, self._tile_height))
        self._o_symbol = pygame.transform.scale(pygame.image.load("o_sign.jpg"), (self._tile_width, self._tile_height))
        self._empty_symbol = pygame.transform.scale(pygame.image.load("empty_sign.png"), (self._tile_width, self._tile_height))

        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        self._font = pygame.font.SysFont('Comic Sans MS', constants.display_font_size)

    def use_menu(self):
        ###self.set_menu_difficulty_chosen(None, constants.ai_easy)
        self._menu.enable()
        self._menu.mainloop(self._screen)
        return self._menu_action_chosen###, self._menu_difficulty_chosen

    def set_menu_play_chosen(self):
        self._menu_action_chosen = constants.menu_play_game
        self._menu.disable()

    def set_menu_exit_chosen(self):
        self._menu_action_chosen = constants.menu_exit
        self._menu.disable()

    def set_menu_difficulty_chosen(self, _, difficulty):
        ###self._menu_difficulty_chosen = difficulty
        ...

    def display_result(self, winner):
        self._screen.fill(constants.white_color)
        text_surface = self._font.render(f"Wins: {winner}.", False, (0, 0, 0))
        self._screen.blit(text_surface, (0, 0))
        pygame.display.update()
        pygame.display.flip()

    def display_board(self, board):
        self._screen.fill(constants.white_color)
        for x in range(board.width):
            for y in range(board.height):
                self._screen.blit(self._x_symbol if board.get_tile((x, y)) == 'x' else (self._o_symbol if board.get_tile((x, y)) == 'o' else self._empty_symbol),
                                  (x * self._tile_width, y * self._tile_height))
        pygame.display.update()
        pygame.display.flip()

    def display_prolog(self, player_symbol):
        self._screen.fill(constants.white_color)
        text_surface = self._font.render(f"You play as: {player_symbol}. Begins: {constants.starting_player}", False, (0, 0, 0))
        self._screen.blit(text_surface, (0, 0))
        pygame.display.update()
        pygame.display.flip()

    def get_events(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                return constants.menu_exit, None, None
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                return constants.mouse_clicked, int(mouse_pos[0]/self._tile_width), int(mouse_pos[1]/self._tile_height)
        return None, None, None

    def __del__(self):
        pygame.quit()
