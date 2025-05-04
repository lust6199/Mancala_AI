import random

class Mancala:
    def __init__(self, pits_per_player=6, stones_per_pit = 4):
        """
        The constructor for the Mancala class defines several instance variables:

        pits_per_player: This variable stores the number of pits each player has.
        stones_per_pit: It represents the number of stones each pit contains at the start of any game.
        board: This data structure is responsible for managing the Mancala board.
        current_player: This variable takes the value 1 or 2, as it's a two-player game, indicating which player's turn it is.
        moves: This is a list used to store the moves made by each player. It's structured in the format (current_player, chosen_pit).
        p1_pits_index: A list containing two elements representing the start and end indices of player 1's pits in the board data structure.
        p2_pits_index: Similar to p1_pits_index, it contains the start and end indices for player 2's pits on the board.
        p1_mancala_index and p2_mancala_index: These variables hold the indices of the Mancala pits on the board for players 1 and 2, respectively.
        """
        self.pits_per_player = pits_per_player
        self.stones_per_pit = stones_per_pit
        self.board = [stones_per_pit] * ((pits_per_player+1) * 2)  # Initialize each pit with stones_per_pit number of stones 
        self.players = 2
        self.current_player = 1
        self.moves = []
        self.p1_pits_index = [0, self.pits_per_player-1]
        self.p1_mancala_index = self.pits_per_player
        self.p2_pits_index = [self.pits_per_player+1, len(self.board)-1-1]
        self.p2_mancala_index = len(self.board)-1
        
        # Zeroing the Mancala for both players
        self.board[self.p1_mancala_index] = 0
        self.board[self.p2_mancala_index] = 0

    def display_board(self):
        """
        Displays the board in a user-friendly format
        """
        player_1_pits = self.board[self.p1_pits_index[0]: self.p1_pits_index[1]+1]
        player_1_mancala = self.board[self.p1_mancala_index]
        player_2_pits = self.board[self.p2_pits_index[0]: self.p2_pits_index[1]+1]
        player_2_mancala = self.board[self.p2_mancala_index]

        print('P1               P2')
        print('     ____{}____     '.format(player_2_mancala))
        for i in range(self.pits_per_player):
            if i == self.pits_per_player - 1:
                print('{} -> |_{}_|_{}_| <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            else:    
                print('{} -> | {} | {} | <- {}'.format(i+1, player_1_pits[i], 
                        player_2_pits[-(i+1)], self.pits_per_player - i))
            
        print('         {}         '.format(player_1_mancala))
        turn = 'P1' if self.current_player == 1 else 'P2'
        print('Turn: ' + turn)

    def valid_move(self, pit):
        """
        Function to check if the pit chosen by the current_player is a valid move.
        Are the pits on my side and do they have any stones in them?
        """
        
        # write your code here
        # convert 1-indexed pit to 0 indexed board index 
        if self.current_player == 1:
            pit_index = pit - 1   # P1 pits: 0 to pits_per_player+1
        else:
            pit_index = pit - 1 + self.pits_per_player + 1 #P2 pits: pits_per_player+1 to len(board)

        #check player 1's move
        if self.current_player == 1:
            #checks if pit is within p1 range
            if pit_index >= self.p1_pits_index[0] and pit_index <= self.p1_pits_index[1]: 
                #checks if pit has stones
                if self.board[pit_index] > 0:
                    return True
            return False
        #check player 2's move
        else:
            #checks if pit is within p2 range
            if pit_index >= self.p2_pits_index[0] and pit_index <= self.p2_pits_index[1]:
                #checks if pit has stones
                if self.board[pit_index] > 0:
                    return True
            return False
            

    def random_move_generator(self):
        """
        Function to generate random valid moves with non-empty pits for the current player.
        Returns: A 1-indexed pit number that has stones.
        """

        #empty list to store valid pits 
        valid_pits = []

        #check each pit
        for pit in range(1, self.pits_per_player + 1):
            if self.valid_move(pit):
                valid_pits.append(pit)

        #return none if no valid pits 
        if not valid_pits:
            return None
        
        #randomly select and return valid pit
        return random.choice(valid_pits)
    

    def play(self, pit):
        """
        This function simulates a single move made by a specific player using their selected pit. It primarily performs three tasks:
        1. It checks if the chosen pit is a valid move for the current player. If not, it prints "INVALID MOVE" and takes no action.
        2. It verifies if the game board has already reached a winning state. If so, it prints "GAME OVER" and takes no further action.
        3. After passing the above two checks, it proceeds to distribute the stones according to the specified Mancala rules.

        Finally, the function then switches the current player, allowing the other player to take their turn.
        """
        
        # write your code here

        # step 1: check if move is valid 
        if not self.valid_move(pit):
            print("INVALID MOVE")
            return self.board

        # step 2: check if game is over

        if self.winning_eval():
            print("GAME OVER")
            return self.board
        
        #records the move
        self.moves.append((self.current_player, pit))

        #converts 1 index pit to 0 index pit 
        if self.current_player == 1:
            pit_index = pit - 1  # P1 pits: 0 to pits_per_player+1
        else:
            pit_index = pit - 1 + self.pits_per_player + 1 #P2 pits: pits_per_player+1 to len(board)

        #pick up all stones in chosen pit 
        stones = self.board[pit_index]
        self.board[pit_index] = 0
        current_index = pit_index
        
        #step 3: distribute stones counter clockwise
        while (stones > 0):
            current_index += 1
            current_index = current_index % len(self.board) #wrap around the board

            #skip opp mancala 
            if self.current_player == 1 and current_index == self.p2_mancala_index:
                continue #moves to next pit without dropping stone
            elif self.current_player == 2 and current_index == self.p1_mancala_index:
                continue #moves to next pit without dropping stone

            #drop one stone in current pit 
            self.board[current_index] += 1 
            stones -= 1
            last_index = current_index #tracks last pit stone was dropped

        #step 4: handles capture if last stone lands in an empty pit on players side 
        if stones == 0:
            if self.current_player == 1:
                #check is last stone lands in p1 empty pit
                if (last_index >= self.p1_pits_index[0] and last_index <= self.p1_pits_index[1]) and self.board[last_index] == 1:
                    opposite_index = (len(self.board) - 2) - last_index #opposite pit index
                    if self.board[opposite_index] > 0: #if opp pit has stones 
                        #capture stones from both pits 
                        captured = self.board[opposite_index] + 1 # include single stone in last_index 
                        self.board[last_index] = 0 #sets landing pit to 0 
                        self.board[opposite_index] = 0 #sets opp pit to 0
                        self.board[self.p1_mancala_index] += captured #adds captured stones to p1's mancala 

            elif self.current_player == 2:
                #check is last stone lands in p2 empty pit
                if (last_index >= self.p2_pits_index[0] and last_index <= self.p2_pits_index[1]) and self.board[last_index] == 1:
                    opposite_index = (len(self.board) - 2) - last_index #opposite pit index 
                    if self.board[opposite_index] > 0: #if opp pit has stones 
                        #capture stones from both pits
                        captured = self.board[opposite_index] + 1 #include 1 stone in last_index 
                        self.board[last_index] = 0 #sets landing pit to 0 
                        self.board[opposite_index] = 0 #sets opp pit to 0
                        self.board[self.p2_mancala_index] += captured #adds captured stones to mancala 

        #switches players
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

        return self.board

    def winning_eval(self):
        """
        Function to verify if the game board has reached the winning state.
        Hint: If either of the players' pits are all empty, then it is considered a winning state.
        """
        #check if all p1 pits are empty
        p1_empty = True 
        for i in range(self.p1_pits_index[0], self.p1_pits_index[1] + 1):
            if self.board[i] != 0:
                p1_empty = False

        #check if all p2 pits are empty 
        p2_empty = True
        for i in range(self.p2_pits_index[0], self.p2_pits_index[1] + 1):
            if self.board[i] != 0:
                p2_empty = False

        #once all of one players pits are empty, the game has reached a terminal state        
        if p1_empty or p2_empty:

            #collects remaining stones from p1 and add them to mancala
            if not p1_empty:
                total = 0
                for i in range(self.p1_pits_index[0], self.p1_pits_index[1] + 1):
                    total += self.board[i]
                    self.board[i] = 0
                self.board[self.p1_mancala_index] += total
            #collects remaining stones from p2 and add them to mancala 
            if not p2_empty:
                total = 0
                for i in range(self.p2_pits_index[0], self.p2_pits_index[1] + 1):
                    total += self.board[i]
                    self.board[i] = 0
                self.board[self.p2_mancala_index] += total

            #determines who wins, if p1 has more stones, p1 wins and if p2 has more stones, p2 wins 
            if self.board[self.p1_mancala_index] > self.board[self.p2_mancala_index]:
                return "P1"
            elif self.board[self.p2_mancala_index] > self.board[self.p1_mancala_index]:
                return "P2"
            else:
                return "Tie" 
        
        #return none if not in terminal state
        return None
    
    def minimax_decision(self, depth):
        #Returns the best pit for the current player using minimax with a given depth
        
        #helper function to eval maximizing players moves
        def max_value(game, depth, player):
            if depth == 0 or game.winning_eval(): #base case, returns utility
                return game.board[game.p1_mancala_index] - game.board[game.p2_mancala_index] #utility function 
            v = float('-inf') #value = -infinity
            game.current_player = player

            #explores all valid moves for current player
            for pit in range(1, game.pits_per_player + 1):
                if game.valid_move(pit):
                    #creates copy of game to simulate move
                    game_copy = Mancala(pits_per_player=game.pits_per_player, stones_per_pit=game.stones_per_pit)
                    game_copy.board = game.board.copy()
                    game_copy.current_player = player
                    game_copy.p1_mancala_index = game.p1_mancala_index
                    game_copy.p2_mancala_index = game.p2_mancala_index
                    game_copy.p1_pits_index = game.p1_pits_index
                    game_copy.p2_pits_index = game.p2_pits_index
                    game_copy.moves = game.moves.copy()
                    game_copy.play(pit)  # This switches player to 3 - player
                    game_copy.current_player = 3 - player  # set to opponent
                    #recursively run through opps response
                    v = max(v, min_value(game_copy, depth - 1, 3 - player))
            return v
        
        #help function to eval minimizing players moves
        def min_value(game, depth, player):
            if depth == 0 or game.winning_eval(): #base case, returns utility 
                return game.board[game.p1_mancala_index] - game.board[game.p2_mancala_index] # utility function 
            v = float('inf') #initialize value = infinity
            game.current_player = player
            
            #explores all valid moves for current player
            for pit in range(1, game.pits_per_player + 1):
                if game.valid_move(pit):
                    #creates copy of game to simulate move
                    game_copy = Mancala(pits_per_player=game.pits_per_player, stones_per_pit=game.stones_per_pit)
                    game_copy.board = game.board.copy()
                    game_copy.current_player = player
                    game_copy.p1_mancala_index = game.p1_mancala_index
                    game_copy.p2_mancala_index = game.p2_mancala_index
                    game_copy.p1_pits_index = game.p1_pits_index
                    game_copy.p2_pits_index = game.p2_pits_index
                    game_copy.moves = game.moves.copy()
                    game_copy.play(pit)  # This switches player to 3 - player
                    game_copy.current_player = 3 - player  # set to opp
                    #recursively run through opps response
                    v = min(v, max_value(game_copy, depth - 1, 3 - player))
            return v

        #initialize to keep track of best move
        best_pit = None
        best_value = float('-inf')
        player = self.current_player

        #eval each move to determine the best
        for pit in range(1, self.pits_per_player + 1):
            if self.valid_move(pit):
                #creates copy of game state 
                game_copy = Mancala(pits_per_player=self.pits_per_player, stones_per_pit=self.stones_per_pit)
                game_copy.board = self.board.copy()
                game_copy.current_player = player
                game_copy.p1_mancala_index = self.p1_mancala_index
                game_copy.p2_mancala_index = self.p2_mancala_index
                game_copy.p1_pits_index = self.p1_pits_index
                game_copy.p2_pits_index = self.p2_pits_index
                game_copy.moves = self.moves.copy()
                game_copy.play(pit)  # This switches player to 3 - player
                game_copy.current_player = 3 - player  # set to opp
                #eval move using Minimax
                value = min_value(game_copy, depth - 1, 3 - player)

                #update best move if this move is better
                if value > best_value:
                    best_value = value
                    best_pit = pit
                
        return best_pit
    
    
    def alpha_beta_decision(self, depth):
    #Returns the best pit for the current player using alpha_beta with a given depth
        
        #help func to eval maximizing players move with pruning
        def alpha_beta_max(game, depth, alpha, beta, player):
            if depth == 0 or game.winning_eval(): #base case, return utility
                return game.board[game.p1_mancala_index] - game.board[game.p2_mancala_index] #utility function 
            v = float('-inf') #value = -infinity
            game.current_player = player

            #eval all valid moves for current player
            for pit in range(1, game.pits_per_player + 1):
                if game.valid_move(pit):
                    #creates copy of game state 
                    game_copy = Mancala(pits_per_player=game.pits_per_player, stones_per_pit=game.stones_per_pit)
                    game_copy.board = game.board.copy()
                    game_copy.current_player = player
                    game_copy.p1_mancala_index = game.p1_mancala_index
                    game_copy.p2_mancala_index = game.p2_mancala_index
                    game_copy.p1_pits_index = game.p1_pits_index
                    game_copy.p2_pits_index = game.p2_pits_index
                    game_copy.moves = game.moves.copy()
                    game_copy.play(pit)  # This switches player
                    game_copy.current_player = 3 - player  # set to opp

                    #recursively eval opp responses
                    v = max(v, alpha_beta_min(game_copy, depth - 1, alpha, beta, 3 - player))
                    
                    #updates alpha to best value of maxes 
                    alpha = max(alpha, v)

                    #prunes if beta <= alpha 
                    if beta <= alpha:
                        break #beta cutoff, skip remaining moves 

            return v

        #help func to eval minimizing players move with pruning
        def alpha_beta_min(game, depth, alpha, beta, player):
            if depth == 0 or game.winning_eval(): # base case, return utility 
                return game.board[game.p1_mancala_index] - game.board[game.p2_mancala_index] #utility function
            v = float('inf') #sets value = infinity
            game.current_player = player

            #eval all valid moves for current player
            for pit in range(1, game.pits_per_player + 1):
                if game.valid_move(pit):
                    #creates copy of game state 
                    game_copy = Mancala(pits_per_player=game.pits_per_player, stones_per_pit=game.stones_per_pit)
                    game_copy.board = game.board.copy()
                    game_copy.current_player = player
                    game_copy.p1_mancala_index = game.p1_mancala_index
                    game_copy.p2_mancala_index = game.p2_mancala_index
                    game_copy.p1_pits_index = game.p1_pits_index
                    game_copy.p2_pits_index = game.p2_pits_index
                    game_copy.moves = game.moves.copy()
                    game_copy.play(pit)  # This switches player
                    game_copy.current_player = 3 - player  #set to opp 

                    #recursively eval opp responses
                    v = min(v, alpha_beta_max(game_copy, depth - 1, alpha, beta, 3 - player))

                    #update beta, best value for min 
                    beta = min(beta, v)

                    #prune if beta <= alpha 
                    if beta <= alpha:
                        break #alpha cutoff, skip remaining moves 

            return v

        #keeps track of best moves
        best_pit = None
        best_value = float('-inf')
        player = self.current_player
        alpha = float('-inf') #initialize alpha for pruning
        beta = float('inf') #initialize beta for pruning

        #eval each move to determine best move 
        for pit in range(1, self.pits_per_player + 1):
            if self.valid_move(pit):
                #creates copy of game state 
                game_copy = Mancala(pits_per_player=self.pits_per_player, stones_per_pit=self.stones_per_pit)
                game_copy.board = self.board.copy()
                game_copy.current_player = player
                game_copy.p1_mancala_index = self.p1_mancala_index
                game_copy.p2_mancala_index = self.p2_mancala_index
                game_copy.p1_pits_index = self.p1_pits_index
                game_copy.p2_pits_index = self.p2_pits_index
                game_copy.moves = self.moves.copy()
                game_copy.play(pit)  #simulates the move
                game_copy.current_player = 3 - player  # set to opp
                #eval move using alpha beta 
                value = alpha_beta_min(game_copy, depth - 1, alpha, beta, 3 - player)

                #update move if this is better 
                if value > best_value:
                    best_value = value
                    best_pit = pit
                
                #update alpha for top level pruning 
                alpha = max(alpha, value)
                
        return best_pit
    
