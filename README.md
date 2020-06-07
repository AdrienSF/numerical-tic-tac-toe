# Numerical tic-tac-toe
This project consists of an engine and agent for playing 3 by 3 numerical tic-tac-toe [[1]](https://en.wikipedia.org/wiki/Tic-tac-toe_variants#Numerical_Tic-tac-toe).

The engine is in the form of a Game() class that holds information about the game (turn count, state of the board...) as well as methods that enable you to play a move and advance the state of the game object. The game object will raise an exception if an illegal move is attempted.

One can choose to run only the engine (multiplayer mode), in which case the main script will ask for user input on every turn. Alternatively, singleplayer mode can be chosen, in which case the main script asks for user input every two turns and gets input form an Agent() object every other turn.

The Agent() class contains an implementation of minimax search along with alpha beta pruning and "good enough" pruning. What I call "good enough" pruning is simply a way of stopping the algorithm from continuing it's search if it has already found a move leading to a winning state (or a move leading to a losing state during minimizing steps). There are no heuristics involved, the game tree is small enough that it is feasible to search all of it in order to find a theoretically perfect strategy (numerical tic-tac-toe is a solved game: [the first player has a winning strategy](https://link.springer.com/chapter/10.1007/978-3-319-08783-2_46)). Despite this feasibility and the optimizations I've implemented, it's still quite slow on your average computer so I've hard-coded the perfect first move (for the first player), drastically reducing the time it takes for the Agent() object to play a full game. If the agent plays first, it will choose to place a 9 in the bottom row middle column. This is the first move of a winning strategy, so as the second player you will be unable to win, no matter how you play the agent will end up winning. On my not-so-powerfull laptop, it takes about a minut for the agent to play the second turn (or third turn depending on which player the agent is), and less than a few seconds for the subsequent turns.

I watched [this](https://www.youtube.com/watch?v=l-hh51ncgDI) video to remind myself of the implementation of minimax search.

## Installation
No dependencies are required to run this project, simply clone or download the repository.

## Usage
Run main.py and you will be asked which mode and which player you wish to play as (odd player goes first). Every turn, the main script will display (as a python dict) all information kept by the game engine, as well as a more readable display of game information (the current board configuration, the pieces available to the user, and an indication of which player's turn it is). The user will be asked to input which piece to place as well as which row and column to place it.

## TODO
This project was completed in under 24 hours as a coding challenge, but given enough time there are a few more things I would have done with best practices in mind.

- add unit test files for the agent and game engine
- make sure the scale of the game (3 by 3) is not hard-coded in the engine and agent, so that they can be easily improved to handle a game of n by n numerical tic-tac-toe
- seperate the planing aspect (minimax search) and the agent into different classes, so that the Agent() class can take different strategies (planner objects) as input
