# [1, 2, 3] | [[0,0], [0,1], [0,2]] wins: all 0 rows, all 0 colm, all 1 rows, all 1 colm 
# [4, 5, 6] | [[1,0], [1,1], [1,2]]       all 2 rows, all 2 colm, 0,0,1,1,2,2 and 0,2,1,1,2,0 corner cases
# [7, 8, 9] | [[2,0], [2,1], [2,2]]

# 3, 12, 21, 9, 11, 15, 12, 12 
# 6, 15, 24, 12, 15, 18, (15, 15)
# 
# idea is to make a 3x3 tictactoe game, we can like append all these combinations 
# in a list and then as the user ticks a section we can pop that out of the list and
# maybe add it to a new list that way we can check for patterns 

#possible wins (it all depends on where the first pointer has been placed on the map)
# [0,1,2] [0,3,6] [0,1,2] [0,1,2] [0,1,2] [0,1,2] [0,1,2] [0,1,2] [0,1,2]
class TicTacToe:
    def __init__(self):
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
        self.player_1 = []
        self.player_2 = []
        self.turn = 0 
        self.winning_combos = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]
    
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = 0
                
    def check_valid_states(self):
        valid_states = []
        for i in range(3):
            state_checker = []
            for j in range(3):
                if self.board[i][j] != 'P1' or self.board[i][j] != 'P2':
                    state_checker.append(self.board[i][j])
            valid_states.append(state_checker)
        return valid_states

    def update_board_state(self, position):
        if self.turn == 0: 
            self.player_1.append(str(position))
            if position <= 3:
                 self.board[0][position - 1] = 'P1'
            elif position <= 6: 
                 self.board[1][position - 4] = 'P1'
            else:
                 self.board[2][position - 7] = 'P1'
        else:
            if self.turn % 2 == 0:
                self.player_1.append(str(position))
                if position <= 3:
                    self.board[0][position - 1] = 'P1'
                elif position <= 6: 
                    self.board[1][position - 4] = 'P1'
                else:
                    self.board[2][position - 7] = 'P1'
            else:
                    self.player_2.append(str(position))
                    if position <= 3:
                        self.board[0][position - 1] = 'P2'
                    elif position <= 6: 
                        self.board[1][position - 4] = 'P2'
                    else:
                        self.board[2][position - 7] = 'P2'
        self.turn += 1 
        return self.player_1, self.player_2, self.board
        
    def check_winner(self):
        for combinations in self.winning_combos:
            if all(x in self.player_1 for x in combinations):
                return 1
            if all(x in self.player_2 for x in combinations):
                return 2
        return 0

    def tictactoe(self, position):
        self.player_1, self.player_2, self.board = self.update_board_state(position)
        if len(self.player_1) >= 3 or len(self.player_2) >= 3:
            verdict = self.check_winner()
            if verdict == 1:
                return "Player 1 Won"
            elif verdict == 2:
                return "Player 2 Won"
        if len(self.player_1) + len(self.player_2) == 9: 
            return f"Match Draw {self.board}"

