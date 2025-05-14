#-------------------------------------------------------------------------------
# Name:        final and test_suite
# Purpose:     The final project is a simple game program that you write and submit to your GitHub repository.
# Author:      robertr
#
# Created:     05/13/2025
# Copyright:   (c) robertr 2025
# Licence:     i don't know what to put here.
#-------------------------------------------------------------------------------

import os

# Clear's game screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Displays game board
def draw_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-" * 5)

# Make an Empty Board
def empty_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Check if a player has won
def has_won(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Convert move (1-9) into board spot
def move_to_board_spot(move):
    return (move - 1) // 3, (move - 1) % 3

# Ask player for a move
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                row, col = move_to_board_spot(move)
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid move. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Save game results
def save_result(result):
    with open("tictactoe_games.txt", "a") as file:
        file.write(result + "\n")

# Main game loop
def main():
    while True:
        board = empty_board()
        current_player = "X"
        clear_screen()
        print("Let's play Tic Tac Toe!")
        print("Player X and Player O take turns.")
        print("Use numbers 1-9 as shown below:")
        print(" 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9\n")

        while True:
            draw_board(board)
            print(f"{current_player}'s turn.")
            row, col = get_player_move(board)
            board[row][col] = current_player

            if has_won(board, current_player):
                clear_screen()
                draw_board(board)
                print(f"{current_player} wins")
                save_result(f"Winner: {current_player}")
                break
            elif is_board_full(board):
                clear_screen()
                draw_board(board)
                print("It's a tie!")
                save_result("Result: Tie")
                break

            current_player = "O" if current_player == "X" else "X"

        again = input("Wanna play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing.")
            break

if __name__ == "__main__":
    main()

# TEST SUITE

# Test move_to_board_spot
print("Testing move_to_board_spot")
print(move_to_board_spot(1) == (0, 0))
print(move_to_board_spot(5) == (1, 1))
print(move_to_board_spot(9) == (2, 2))

# Test has_won
print("Testing has_won")

board_row_win = [
    ["X", "X", "X"],
    [" ", "O", " "],
    ["O", " ", " "]
]
print(has_won(board_row_win, "X") == True)

board_col_win = [
    ["O", "X", " "],
    ["O", "X", " "],
    ["O", " ", "X"]
]
print(has_won(board_col_win, "O") == True)

board_diag_win = [
    ["X", "O", " "],
    ["O", "X", " "],
    [" ", " ", "X"]
]
print(has_won(board_diag_win, "X") == True)

# Test is_board_full
print("Testing is_board_full")
full_board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "O"]
]
print(is_board_full(full_board) == True)

not_full_board = [
    ["X", "O", " "],
    ["O", "X", "O"],
    ["O", "X", "O"]
]
print(is_board_full(not_full_board) == False)