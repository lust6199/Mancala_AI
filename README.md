# Mancala AI Game

## Overview
This project implements an AI-driven Mancala game where three different methods of play are tested and runtimes are recorded. Mancala is a classic two-player board game, and this implementation focuses on developing intelligent AI models to play against a player who's moves are randomly generated. I built this as my final project in the class, Intro to Artifical Intelligence, to explore game AI concepts and improve my skills in Python programming and algorithm design.

## Key Features
- **Simulated Mancala Game**: Fully functional game logic for Random vs. Random, Minimax vs. Random, and Alpha-Beta vs. Random gameplay.
- **AI Strategies**:
  - **Random Move Generator**: AI selects moves randomly as a baseline opponent.
  - **Minimax Decision**: AI uses the minimax algorithm to make optimal moves by evaluating future game states.
  - **Alpha-Beta Pruning**: Optimizes the Minimax Decision algorithm for faster performance.
- **Runtime Analysis**: Records and compares the runtimes of different AI strategies.

## Rules of Mancala Implemented
- Players sit on opposite sides of the long edge of the board
- There are 6 small pits in the middle of the board and 2 large ones at each end.
- The small ones in the middle and the large pit on your right are yours. The small
ones on the other side and the large pit to your opponent's right are theirs
- The large pits at the end of the board are called Mancalas
- Set up the board with 4 stones per small pit (none in the mancalas)
- On every turn, select a pit on your side of the board that contains one or more
stones, then distribute its stones, one stone per pit, in an counter-clockwise
direction until you have no stones remaining
- If you encounter your opponent's mandala, skip it
- If you encounter your mancala, drop a stone into it
- If the last stone lands in an empty pit on your side of the board, capture this
stone and any stones in your opponent's pit on the other side of the board,
collect all of these stones, including the one that just landed, and place them
into your mancala.
- If either player's pits are entirely empty, the game concludes.
- The player who still has stones on his side of the board when the game
concludes places all of these pieces into their mancala.
- The player with the most stones in their mancala is declared the winner. If both
players have an equal number of stones in their mancala, the game results in a
tie.

## Tech Stack
- **Language**: Python
- **Algorithms**: Minimax, Alpha-Beta, Random Move Selection
- **Tools**: Git for version control

## How It Works
1. **Installation**:
   - Clone the repository: `git clone https://github.com/lust6199/Mancala_AI.git`
   - Navigate to the project directory: `cd Mancala_AI`
   - Ensure Python 3.x is installed.
2. **Run the Game**:
   - Execute the main script: `python Mancala_Main.py`
   - View the results of Random vs. Random, Minimax vs. Random, and Alpha-Beta vs. Random gameplay, including runtime comparisons.

## Code Provided for the Project
Within the `Mancala` class:
- `def __init__(self, pits_per_player=6, stones_per_pit=4)`: Initializes the Mancala board.
- `def display_board(self)`: Displays the current state of the board.

## My Contributions
- Designed and implemented the core game logic for Mancala, including all the rules listed above.
- Developed key functions: `play`, `winning_eval`, `game_play`, `minimax_decision`, `alpha_beta_decision`, and `main`.
- Developed two AI strategies: Minimax Decision and Alpha-Beta Decision
- Condensed three gameplay modes (Random vs. Random, Minimax vs. Random, Alpha-Beta vs. Random) into a single `game_play` function.
- Added detailed comments to explain complex logic, improving code readability and maintainability.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/lucas-stackhouse) or check out my other projects on [GitHub](https://github.com/lust6199).
