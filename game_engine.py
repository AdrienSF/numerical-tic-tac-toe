from enum import Enum

class Player(Enum):
    ODD = 1
    EVEN = 0

class State(Enum):
    CONTINUE = 0
    ODD_WIN = 1
    EVEN_WIN = 2
    DRAW = 3

class Game():
    def __init__(self):
        self.turn_count = 1
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.even_pieces = {2: 2, 4: 4, 6: 6, 8: 8}
        self.odd_pieces = {1: 1, 3: 3, 5: 5, 7: 7, 9: 9}
        self.player_turn = Player.ODD
        self.state = State.CONTINUE

    def play(self, piece: int, row: int, col: int, player=None):
        # player is an optional parameter, the game object already knows who's turn it is if none is provided
        if not player:
            player = self.player_turn

        # check game is not finished
        if self.state != State.CONTINUE:
            raise Exception("game is not in play, state is: " + str(self.state))
        # check player turn is correct
        if player != self.player_turn:
            raise Exception("turn should be " + str(self.player_turn) + " but was given " + str(player))
        # check board position is valid and free
        if not ((row <= 3 and row >= 0) and (col <=3 and col >= 0)):
            raise Exception("row: " + str(row) + " column: " + str(col) + "is not a valid board position")
        if self.board[row][col]:
            raise Exception("row: " + str(row) + " col: " + str(col) + " already occupied")

        # check the player has the piece, if so remove piece from available pieces
        if player == Player.ODD:
            if piece in self.odd_pieces and self.odd_pieces[piece]:
                self.odd_pieces[piece] = None
            else:
                raise Exception(str(player) + " does not have piece: " + str(piece) + " to play")
        else:
            if piece in self.even_pieces and self.even_pieces[piece]:
                self.even_pieces[piece] = None
            else:
                raise Exception(str(player) + " does not have piece: " + str(piece) + " to play")

        # place piece
        self.board[row][col] = piece
        # check if the game has ended
        self.set_game_state()
        # advance turn
        self.turn_count += 1
        self.player_turn = Player(self.turn_count % 2) # odd player plays on odd turns, even player on even turns
        # return all info about the game
        return self.__dict__


    def set_game_state(self):
        # check game is not finished
        if self.state != State.CONTINUE:
            raise Exception("game is not in play, state is: " + str(self.state))
            return

        # if any of the rows, columns or diagonals add up to 15, the player whose current turn it is won
        colunms = [ [ row[i] for row in self.board ] for i in range(len(self.board[0])) ]
        diagonals = [[ self.board[i][i] for i in range(len(self.board)) ], [ self.board[i][len(self.board[0])-1-i] for i in range(len(self.board)) ]]
        lines = self.board + colunms + diagonals

        if any([ sum(line) == 15 for line in lines if all(line) ]):
            # then current player won
            if self.player_turn == Player.ODD:
                self.state = State.ODD_WIN
            else:
                self.state = State.EVEN_WIN
        # if no one won, check if board is full (players have no pieces left), if so it's a draw
        elif not any(self.odd_pieces.values()) and not any(self.even_pieces.values()):
            self.state = State.DRAW

        # if neither of these cases apply, remain in a continue state

        

        
        