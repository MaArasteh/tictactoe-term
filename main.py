import time
import random

startup2 = r"""
 _____ _        _____            _____          
|_   _(_) ___  |_   _|_ _  ___  |_   _|__   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \
  | | | | (__    | | (_| | (__    | | (_) |  __/
  |_| |_|\___|   |_|\__,_|\___|   |_|\___/ \___|
"""

table = " 1 | 2 | 3 \n"
table += "-----------\n"
table += " 4 | 5 | 6\n"
table += "-----------\n"
table += " 7 | 8 | 9\n"

print(startup)
time.sleep(1)
print(startup2)

print("Do you really want to play the game (Options: yes, y, no, n)")
yes_no = input(">> ").strip().lower()

if yes_no not in ["yes", "y"]:
    exit()

print("Do you know how to play with terminal?")
yes_no_2 = input(">> ").strip().lower()
if yes_no_2 in ["no", "n"]:
    print(r"""
 _   _                 __  __                         _ 
| | | |___  ___ _ __  |  \/  | __ _ _ __  _   _  __ _| |
| | | / __|/ _ \ '__| | |\/| |/ _` | '_ \| | | |/ _` | |
| |_| \__ \  __/ |    | |  | | (_| | | | | |_| | (_| | |
 \___/|___/\___|_|    |_|  |_|\__,_|_| |_|\__,_|\__,_|_|""")
    time.sleep(2)
    print("""Welcome to TicTacToe terminal game
          To put an X or O (anything selected randomly), type number in table you want to catch in input
          Nothing else""")

def print_table(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

randnum = random.randint(0, 1)
if randnum == 0:
    person = "X"
    robot = "O"
    print("You are X")
else:
    person = "O"
    robot = "X"
    print("You are O")

time.sleep(2)

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print_table(board)

moves = 0
while moves < 9:
    num = input(">> ").strip()
    if num not in board:
        print("Invalid move, try again.")
        continue

    board[int(num) - 1] = person
    print_table(board)
    moves += 1

    if check_win(board, person):
        print("Congratulations! You W-O-N!")
        break

    if moves == 9:
        print("It's a draw!")
        break

    print("Robot's turn...")
    time.sleep(1.5)
    robotoption = random.choice([x for x in board if x.isdigit()])
    board[int(robotoption) - 1] = robot
    print_table(board)
    moves += 1

    if check_win(board, robot):
        print("Game ended. You F-A-I-L-E-D")
        break

if moves == 9 and not check_win(board, person) and not check_win(board, robot):
    print("It's a draw!")
