from game_engine import Game
from game_engine import State
from game_engine import Player
from agent import Agent


    


def singleplayer(game: Game):
    if input("enter e to play as even, o to play as odd: ") == 'e':
        user = Player.EVEN
        agent = Agent(Player.ODD)
    else:
        user = Player.ODD
        agent = Agent(Player.EVEN)


    # show game state at the start of the game
    game_info = game.__dict__
    print(game_info)
    while game.state == State.CONTINUE:
        # print board
        for row in game.board:
            print(row)

        if game.player_turn == user: # get user input
            # Display player's turn, pieces left... and input move
            if user == Player.ODD:
                player = '[odd]'
                pieces_left = [ piece for piece in game.odd_pieces.values() if piece ]
            else:
                player = '[even]'
                pieces_left = [ piece for piece in game.even_pieces.values() if piece ]

            piece = int(input(player +  " select piece to play: (options: " + str(pieces_left) + ") "))
            row = int(input(player +  " select row to place piece: "))
            column = int(input(player +  " select column to place piece: "))
            # move = agent.get_legal_moves(game)[-1]
            # piece = move['piece']
            # row = move['row']
            # column = move['col']

        else: # get agent input
            move = agent.get_move(game)
            piece = move['piece']
            row = move['row']
            column = move['col']

        game_info = game.play(piece, row, column)
        print(game_info)


    # show end of game message and final board configuration
    if game.state == State.EVEN_WIN:
        print('even player won:')
    elif game.state == State.ODD_WIN:
        print('odd player won:')
    else:
        print('draw:')

    for row in game.board:
            print(row)






def multiplayer(game: Game):
    # show game state at the start of the game
    print(game.__dict__)
    while game.state == State.CONTINUE:
        # print board
        for row in game.board:
            print(row)

        # Display player's turn, pieces left... and input move
        if game.player_turn == Player.ODD:
            player = '[odd]'
            pieces_left = [ piece for piece in game.odd_pieces.values() if piece ]
        else:
            player = '[even]'
            pieces_left = [ piece for piece in game.even_pieces.values() if piece ]

        piece = int(input(player +  " select piece to play: (options: " + str(pieces_left) + ") "))
        row = int(input(player +  " select row to place piece: "))
        column = int(input(player +  " select column to place piece: "))
        print(game.play(piece, row, column))

    # show end of game message and final board configuration
    if game.state == State.EVEN_WIN:
        print('even player won:')
    elif game.state == State.ODD_WIN:
        print('odd player won:')
    else:
        print('draw:')

    for row in game.board:
            print(row)


game = Game()
if input("enter m to play multiplayer, s to play singleplayer: ") == 'm':
    multiplayer(game)
else:
    singleplayer(game)