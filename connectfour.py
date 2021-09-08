import numpy as np
import pygame

HEIGHT_BOARD = 6
WIDTH_BOARD = 7
SQUARE_SIZE = 100
HEIGHT_SCREEN = HEIGHT_BOARD * SQUARE_SIZE
WIDTH_SCREEN = WIDTH_BOARD * SQUARE_SIZE


class ConnectFourBoard:
    def __init__(self):
        self.board = np.zeros((HEIGHT_BOARD, WIDTH_BOARD))
        pygame.init()

    def is_valid_location(self, col: int):
        """
        check board(5, col) is enough because we drop from row 0 so if board(5, col) is empty mean
        that this column still have empty position
        :param col: int
        :return: bool
        """
        return self.board[5][col] == 0

    def drop_piece(self, row: int, col: int, piece: int):
        """
        :param row: int
        :param col: int
        :param piece: int
        :return: None
        """
        self.board[row][col] = piece

    def get_next_open_row(self, col: int):
        """
        find empty position in column
        :param col: int
        :return: int
        """
        for row in range(HEIGHT_BOARD):
            if self.board[row][col] == 0:
                return row

    def print_board(self):
        """
        :return: None
        """
        print(np.flip(self.board, 0))

    def play(self, col: int, piece: int):
        """
        :param col: int
        :param piece: int
        :return: None
        """
        if self.is_valid_location(col):
            row = self.get_next_open_row(col)
            self.drop_piece(row, col, piece)
        if self.winning_state():
            print("Player", piece, "win!!! Congrats!!")
            raise Exception("game over!")

    def winning_state(self):
        """
        :return: bool
        """
        # check horizontal locations for win
        for row in range(HEIGHT_BOARD):
            for col in range(WIDTH_BOARD - 3):
                if self.board[row][col] != 0 \
                        and self.board[row][col] == self.board[row][col + 1] \
                        == self.board[row][col + 2] == self.board[row][col + 3]:
                    return True
        # check for vertical locations for win
        for row in range(HEIGHT_BOARD - 3):
            for col in range(WIDTH_BOARD):
                if self.board[row][col] != 0 \
                        and self.board[row][col] == self.board[row + 1][col] \
                        == self.board[row + 2][col] == self.board[row + 3][col]:
                    return True
        # check for positively slope diagonal for win
        for row in range(HEIGHT_BOARD - 3):
            for col in range(WIDTH_BOARD - 3):
                if self.board[row][col] != 0 \
                        and self.board[row][col] == self.board[row + 1][col + 1] \
                        == self.board[row + 2][col + 2] == self.board[row + 3][col + 3]:
                    return True
        # check for negative slope diagonal for win
        for row in range(HEIGHT_BOARD - 3):
            for col in range(3, WIDTH_BOARD):
                if self.board[row][col] == 0 \
                        and self.board[row][col] == self.board[row + 1][col - 1] \
                        == self.board[row + 2][col - 2] == self.board[row + 3][col - 3]:
                    return True

    def play_game(self):
        """
        run the game
        :return: None
        """
        game_over = False
        turn = 0
        while not game_over:
            self.print_board()
            print("Player", turn + 1, "make you selection(0, 6)")
            select_col = int(input())
            try:
                self.play(select_col, turn + 1)
            except Exception as e:
                game_over = True
            turn += 1
            turn = turn % 2


if __name__ == "__main__":
    game = ConnectFourBoard()
    game.play_game()
