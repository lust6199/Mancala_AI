from Mancala_Gameplay import game_play

# MAIN

if __name__ == "__main__":
    print(f"")
    game_play(strategy="random", num_games=10000)
    print(f"")
    game_play(strategy="minimax", num_games=10, depth=10)
    print(f"")
    game_play(strategy="alpha-beta", num_games=10, depth=10)
    print(f"")
    