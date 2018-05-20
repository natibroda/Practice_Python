# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a draft version of Tic Tac Toe game.
"""

from IPython.display import clear_output

# Step 1: Write a function that can print out a board.
 
''' Set up your board as a list, where each index 1-9 corresponds to a number 
on a number pad, so you get a 3 by 3 board representation.
In my representation, 1 is in the top left corner and 9 in the bottom right 
corner (seems more logical to me and I don't use numpad).'''

def display_board(board):
    clear_output()
    string1 = " " + board[1] + " | " + board[2] + " | " + board[3] + " "
    string2 = "-----------"
    string3 = " " + board[4] + " | " + board[5] + " | " + board[6] + " "
    string4 = "-----------"
    string5 = " " + board[7] + " | " + board[8] + " | " + board[9] + " "
    
    print(f"{string1}\n{string2}\n{string3}\n{string4}\n{string5}")
    
# Step 2: Write a function that can take in a player input and assign their 
# marker as 'X' or 'O'. 
# Use while loops to continually ask until you get a correct answer.
    
def player_input():
    player1 = ''
    player2 = 'X'
    while player1 != 'X' and player1 != 'O':
        player1 = input("Do you want to be 'X' or 'O': ").upper()
    if player1 == 'X':
        player2 = 'O'
    print(f"Player 1 is {player1}, Player 2 is {player2}.")
    return (player1, player2)

# Step 3: Write a function that takes in the board list object, a marker 
# ('X' or 'O'),and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker
    return board

# Step 4: Write a function that takes in a board and a mark (X or O) 
# and then checks to see if that mark has won.
    
def win_check(board, mark):
    # Consider all winning options
    win1 = (board[1] == mark and board[2] == mark and board[3] == mark)
    win2 = (board[4] == mark and board[5] == mark and board[6] == mark)
    win3 = (board[7] == mark and board[8] == mark and board[9] == mark)
    win4 = (board[1] == mark and board[4] == mark and board[7] == mark)
    win5 = (board[2] == mark and board[5] == mark and board[8] == mark)
    win6 = (board[3] == mark and board[6] == mark and board[9] == mark)
    win7 = (board[1] == mark and board[5] == mark and board[9] == mark)
    win8 = (board[3] == mark and board[5] == mark and board[7] == mark)
    return (win1 or win2 or win3 or win4 or win5 or win6 or win7 or win8)    

# Step 5: Write a function that uses the random module to randomly decide 
# which player goes first. You may want to lookup random.randint() 
# Return a string of which player went first.
    
from random import randint

def choose_first():
    number = randint(1,2)
    if number == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    
# Step 6: Write a function that returns a boolean indicating whether a space 
# on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns 
# a boolean value. True if full, False otherwise.

def full_board_check(board):
    for i in range(1, len(board)):
        if space_check(board, i):
            return False
    return True

# Step 8: Write a function that asks for a player's next position 
# (as a number 1-9) and then uses the function from step 6 to check if it's 
# a free position. If it is, then return the position for later use.

def player_choice(board):
    position = int(input('Please enter a number: '))
    while space_check(board, position) == False:
        position = int(input('Position already taken. Please enter diferent a number: '))
    return position

# Step 9: Write a function that asks the player if they want to play again 
# and returns a boolean True if they do want to play again.

def replay():
    play_again = input('Would you like to play again? (y/n): ')
    if play_again == 'y':
        return True
    else:
        return False
    
# Make a game

'''We need to print a board.
Take in player input.
Place their input on the board.
Check if the game is won,tied, lost, or ongoing.
Repeat c and d until the game has been won or tied.
Ask if players want to play again.'''

# While game is on
game_on = True

while game_on:
# Display welcome message and the board
        print("Welcome to Tic Tac Toe!")
        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        display_board(board)
# Ask player 1 for marker
        markers = player_input()
# Use counter turn to identify which player's move it is
        turn = 1
# Randomly choose which player goes first
        first = choose_first()
        if first == "Player 1":
            turn = 1
        else:
            turn = 2
        print(f"{first} goes first.")
# Check if board full, if not, ask for position
        while not full_board_check(board):
            if turn % 2 != 0:
                player = markers[0]
            else:
                player = markers[1]
            position = player_choice(board)
            board = place_marker(board, player, position)
            display_board(board)
# Check if player won
            if win_check(board, player) == True:
                print("Congratulations! You won the game!")
                break
            else:
                turn += 1
                continue
        
        game_on = replay()

