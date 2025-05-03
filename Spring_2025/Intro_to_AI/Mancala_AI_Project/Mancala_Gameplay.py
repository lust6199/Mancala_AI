from Mancala_Class import Mancala
import time

def game_play(strategy = "random", depth = 5, num_games = 500):

    start = time.time()

    p1_wins = 0
    p2_wins = 0
    ties = 0
    total_moves_list = []

    for _ in range(num_games):
        game = Mancala(pits_per_player=6, stones_per_pit=4)
        moves_in_game = 0

        while True:
            result = game.winning_eval()
            if result:
                if result == "P1":
                    p1_wins += 1
                elif result == "P2":
                    p2_wins += 1
                else:
                    ties += 1
                total_moves_list.append(moves_in_game)
                break

            game.current_player = 1

            #determines player 1's method 
            if strategy == "random":
                pit = game.random_move_generator()
            elif strategy == "minimax":
                pit = game.minimax_decision(depth)
            elif strategy == "alpha-beta":
                pit = game.alpha_beta_decision(depth)
            else:
                raise ValueError("Invalid strategy")

            if pit is None:
                break

            game.play(pit)
            moves_in_game += 1

            result = game.winning_eval()
            
            if result:
                if result == "P1":
                    p1_wins += 1
                elif result == "P2":
                    p2_wins += 1
                else:
                    ties += 1
                total_moves_list.append(moves_in_game)
                break

            game.current_player = 2

            pit = game.random_move_generator()

            if pit is None:
                break

            game.play(pit)
            moves_in_game += 1

    #game stats
    total_games_played = p1_wins + p2_wins + ties
    p1_win_percent = (p1_wins / total_games_played) * 100
    p2_win_percent = (p2_wins / total_games_played) * 100
    tie_percent = (ties / total_games_played) * 100
    avg_moves = sum(total_moves_list) / len(total_moves_list) if total_moves_list else 0

    #naming logic for print statement 
    if strategy == "random":
        strategy_display = "Random"
    elif strategy == "minimax":
        strategy_display = "Minimax"
    else:
        strategy_display = "Alpha-Beta"

    #runtime, start to finish 
    runtime = time.time() - start

    #final print statements
    print(f"{strategy_display} (P1) vs Random (P2) ({num_games} games, depth={depth if strategy in ['minimax', 'alpha-beta'] else 'N/A'}):")
    print(f"P1 wins: {p1_wins} ({p1_win_percent:.2f}%)")
    print(f"P2 wins: {p2_wins} ({p2_win_percent:.2f}%)")
    print(f"Ties: {ties} ({tie_percent:.2f}%)")
    print(f"Average moves per game: {avg_moves:.2f}")
    print(f"Runtime: {runtime:.2f} seconds")


# def play_random_vs_random():

#     start = time.time()

#     #track wins and ties
#     p1_wins = 0
#     p2_wins = 0
#     ties = 0
#     total_moves_list = [] #list to store number of moves per game 

#     for game_num in range(10000): # run 10,000 games to get good stats
#         game = Mancala(pits_per_player=6, stones_per_pit=4) 
#         moves_in_game = 0

#         while True:
#             result = game.winning_eval() #checks if someone has won or not

#             #update win/tie count based on results
#             if result:
#                 if result == "P1":
#                     p1_wins += 1
#                 elif result == "P2":
#                     p2_wins += 1
#                 else:
#                     ties += 1
#                 total_moves_list.append(moves_in_game) #saves number of moves per game 
#                 break #game over
            
#             game.current_player = 1 #p1 turn 
#             pit = game.random_move_generator() #picks a random and valid pit for p1
#             if pit is None: #no valid moves left 
#                 break
#             game.play(pit) #move is made, switches to p2 automatically 
#             moves_in_game += 1 # counts moves 

#             #checks if p1 move has ended the game
#             result = game.winning_eval()
#             if result:
#                 if result == "P1":
#                     p1_wins += 1
#                 elif result == "P2":
#                     p2_wins += 1
#                 else:
#                     ties += 1
#                 total_moves_list.append(moves_in_game)
#                 break
            
#             #p2 turn
#             game.current_player = 2 
#             pit = game.random_move_generator() #pick random pit for p2
#             if pit is None: #no valid moves left
#                 break
#             game.play(pit) #p2 plays, switches to p1 automatically 
#             moves_in_game += 1 #count moves 

#     # results with %
#     total_games_played = p1_wins + p2_wins + ties
#     p1_win_percent = (p1_wins / total_games_played) * 100
#     p2_win_percent = (p2_wins / total_games_played) * 100
#     tie_percent = (ties / total_games_played) * 100
#     avg_moves = sum(total_moves_list) / len(total_moves_list) if total_moves_list else 0
    
#     runtime = time.time() - start

#     #print results 
#     print(f"Random vs Random (10,000 games):")
#     print(f"P1 wins: {p1_wins} ({p1_win_percent:.2f}%)")
#     print(f"P2 wins: {p2_wins} ({p2_win_percent:.2f}%)")
#     print(f"Ties: {ties} ({tie_percent:.2f}%)")
#     print(f"Average moves per game: {avg_moves:.2f}")
#     print(f"Runtime: {runtime:.2f} seconds")

# def play_minimax_vs_random(depth=3):
#     start = time.time()

#     p1_wins = 0
#     p2_wins = 0
#     ties = 0
#     total_moves_list = []

#     for _ in range(500):
#         game = Mancala(pits_per_player=6, stones_per_pit=4)
#         moves_in_game = 0

#         while True:
#             result = game.winning_eval()
#             if result:
#                 if result == "P1":
#                     p1_wins += 1
#                 elif result == "P2":
#                     p2_wins += 1
#                 else:
#                     ties += 1
#                 total_moves_list.append(moves_in_game)
#                 break

#             game.current_player = 1
#             # if game_num == 0 and moves_in_game < 5:
#             #     print(f"\nBefore P1 move (game {game_num + 1}, move {moves_in_game + 1}):")
#             #     game.display_board()
#             pit = game.minimax_decision(depth)

#             if pit is None:
#                 break
#             # print(f"P1 (minimax) picks pit: {pit}")

#             game.play(pit)
#             moves_in_game += 1

#             result = game.winning_eval()
#             if result:
#                 if result == "P1":
#                     p1_wins += 1
#                 elif result == "P2":
#                     p2_wins += 1
#                 else:
#                     ties += 1
#                 total_moves_list.append(moves_in_game)
#                 break

#             game.current_player = 2
#             # if game_num == 0 and moves_in_game < 5:
#             #     print(f"\nBefore P2 move (game {game_num + 1}, move {moves_in_game + 1}):")
#             #     game.display_board()

#             pit = game.random_move_generator()

#             if pit is None:
#                 break
#             # print(f"P2 (random) picks pit: {pit}")

#             game.play(pit)
#             moves_in_game += 1

#     total_games_played = p1_wins + p2_wins + ties
#     p1_win_percent = (p1_wins / total_games_played) * 100
#     p2_win_percent = (p2_wins / total_games_played) * 100
#     tie_percent = (ties / total_games_played) * 100
#     avg_moves = sum(total_moves_list) / len(total_moves_list) if total_moves_list else 0

#     runtime = time.time() - start

#     print(f"Minimax (P1) vs Random (P2) (500 games, depth={depth}):")
#     print(f"P1 wins: {p1_wins} ({p1_win_percent:.2f}%)")
#     print(f"P2 wins: {p2_wins} ({p2_win_percent:.2f}%)")
#     print(f"Ties: {ties} ({tie_percent:.2f}%)")
#     print(f"Average moves per game: {avg_moves:.2f}")
#     print(f"Runtime: {runtime:.2f} seconds")

# def play_alphabeta_vs_random(depth=3):

#     start = time.time()

#     p1_wins = 0
#     p2_wins = 0
#     ties = 0
#     total_moves_list = []

#     for _ in range(500):
#         game = Mancala(pits_per_player=6, stones_per_pit=4)
#         moves_in_game = 0

#         while True:
#             result = game.winning_eval()
#             if result:
#                 if result == "P1":
#                     p1_wins += 1
#                 elif result == "P2":
#                     p2_wins += 1
#                 else:
#                     ties += 1
#                 total_moves_list.append(moves_in_game)
#                 break

#             game.current_player = 1
#             # if game_num == 0 and moves_in_game < 5:
#             #     print(f"\nBefore P1 move (game {game_num + 1}, move {moves_in_game + 1}):")
#             #     game.display_board()
#             pit = game.alpha_beta_decision(depth)

#             if pit is None:
#                 break
#             # print(f"P1 (alphabeta) picks pit: {pit}")

#             game.play(pit)
#             moves_in_game += 1

#             result = game.winning_eval()
#             if result:
#                 if result == "P1":
#                     p1_wins += 1
#                 elif result == "P2":
#                     p2_wins += 1
#                 else:
#                     ties += 1
#                 total_moves_list.append(moves_in_game)
#                 break

#             game.current_player = 2
#             # if game_num == 0 and moves_in_game < 5:
#             #     print(f"\nBefore P2 move (game {game_num + 1}, move {moves_in_game + 1}):")
#             #     game.display_board()

#             pit = game.random_move_generator()

#             if pit is None:
#                 break
#             # print(f"P2 (random) picks pit: {pit}")

#             game.play(pit)
#             moves_in_game += 1

#     total_games_played = p1_wins + p2_wins + ties
#     p1_win_percent = (p1_wins / total_games_played) * 100
#     p2_win_percent = (p2_wins / total_games_played) * 100
#     tie_percent = (ties / total_games_played) * 100
#     avg_moves = sum(total_moves_list) / len(total_moves_list) if total_moves_list else 0

#     runtime = time.time() - start

#     print(f"Alpha-Beta (P1) vs Random (P2) (500 games, depth={depth}):")
#     print(f"P1 wins: {p1_wins} ({p1_win_percent:.2f}%)")
#     print(f"P2 wins: {p2_wins} ({p2_win_percent:.2f}%)")
#     print(f"Ties: {ties} ({tie_percent:.2f}%)")
#     print(f"Average moves per game: {avg_moves:.2f}")
#     print(f"Runtime: {runtime:.2f} seconds")


