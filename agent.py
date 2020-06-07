from game_engine import Game
from game_engine import State
from game_engine import Player
import copy


class Agent():

    def __init__(self, player: Player):
        self.player = player

    def get_move(self, game: Game):
        legal_moves = self.get_legal_moves(game)
        evaluated_moves = {}
        if game.turn_count <= 1: # if the agent plays the first move, I've hard-coded a perfect move
            perfect_move = {
                'piece': 9,
                'row': 2,
                'col': 1
            }
            return perfect_move
        else:
            for move in legal_moves:
                possible_game = copy.deepcopy(game)
                possible_game.play(move['piece'], move['row'], move['col'])
                evaluated_moves[self.minimax(possible_game, float('-inf'), float('inf'))] = move

            best_value = max(evaluated_moves.keys())
            best_move = evaluated_moves[best_value]
            print("best move has a value of: " + str(best_value))
            return best_move


    def get_legal_moves(self, game: Game):
        if game.state != State.CONTINUE:
            raise Exception("no moves are possible, the game is over")

        if game.player_turn == Player.ODD:
            pieces = [ piece for piece in game.odd_pieces.values() if piece ]
        else:
            pieces = [ piece for piece in game.even_pieces.values() if piece ]
        
        empty_spaces = [ { 'row': i, 'col': j } for i in range(len(game.board)) for j in range(len(game.board)) if not game.board[i][j] ]

        possible_moves = [ { 'piece': piece, 'row': space['row'], 'col': space['col'] } for piece in pieces for space in empty_spaces ]

        return possible_moves


    def minimax(self, game: Game, alpha, beta):
        # base case: the game has ended
        # get the winner
        if game.state != State.CONTINUE:
            if game.state == State.ODD_WIN:
                winner = Player.ODD
            elif game.state == State.EVEN_WIN:
                winner = Player.EVEN
            else:
                winner = None
            # values: win: 1, loss: -1, draw: 0
            if winner:
                if winner == self.player:
                    return 1
                else:
                    return -1
            else:
                return 0


        # if the game is still in play, create every possible game one move in the future
        possible_moves = self.get_legal_moves(game)
        possible_games = []
        for move in possible_moves:
            possible_game = copy.deepcopy(game)
            possible_game.play(move['piece'], move['row'], move['col'])
            possible_games.append(possible_game)

        # check if it's the maximizing or minimizing turn
        if self.player == game.player_turn: # maximizing turn
            max_eval = float('-inf')
            for possible_game in possible_games:
                eval = self.minimax(possible_game, alpha, beta)
                max_eval = max([max_eval, eval])
                alpha = max([alpha, eval])
                if beta <= alpha:
                    break # alpha beta pruning
                if max_eval >= 1: 
                    # a winning configuration has been found, no need to keep looking for better
                    break

            return max_eval

        else: # minimizing turn
            min_eval = float('inf')
            for possible_game in possible_games:
                eval = self.minimax(possible_game, alpha, beta)
                min_eval = min([min_eval, eval])
                beta = min([beta, eval])
                if beta <= alpha:
                    break # pruning
                if min_eval <= -1:
                    # a losing configuration has been found, no need to keep looking for worse
                    break
            
            return min_eval


