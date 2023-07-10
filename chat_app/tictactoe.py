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
player_1 = []
player_2 = []
winning_combos = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]

def user_input(turn, total_turns):
    if turn == 0: 
        player_input_1 = input("Player_1 Enter Position: ")
        player_1.append(player_input_1)
        total_turns.append(player_input_1)
    else:
        if turn % 2 == 0:
            while True:
                player_input_1 = input("Player_1 Enter Position: ")
                if player_input_1 in player_1 or player_input_1 in player_2:
                    print("Retry")
                else:
                    player_1.append(player_input_1)
                    total_turns.append(player_input_1)
                    break

        else:
            while True:
                player_input_2 = input("Player_2 Enter Position: ")
                if player_input_2 in player_1 or player_input_2 in player_2:
                    print("Retry")
                else:
                    player_2.append(player_input_2)
                    total_turns.append(player_input_2)
                    break

    return player_1, player_2, total_turns
    
def check_winner(player_1, player_2):
    for combinations in winning_combos:
        if all(x in player_1 for x in combinations):
            return 1
        if all(x in player_2 for x in combinations):
            return 2
    return 0

def tictactoe():
    total_turns = []
    for i in range(9):
        player_1, player_2, total_turns = user_input(i, total_turns)
        if len(player_1) >= 3 or len(player_2) >= 3:
            verdict = check_winner(player_1, player_2)
            if verdict == 1:
                print("Player 1 Won")
                break
            elif verdict == 2:
                print("Player 2 Won")
                break
        if len(player_1) + len(player_2) == 9: 
            print("Match Draw")
            break

tictactoe()