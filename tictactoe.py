#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9

from random import choice

def check_line(board, player):
    # win = 0
    status = 1
    if (board[0] == board[1] == board[2]) or \
       (board[3] == board[4] == board[5]) or \
       (board[6] == board[7] == board[8]) or \
       (board[0] == board[3] == board[6]) or \
       (board[1] == board[4] == board[7]) or \
       (board[2] == board[5] == board[8]) or \
       (board[0] == board[4] == board[8]) or \
       (board[2] == board[4] == board[6]):
           status = 0
    return status

def print_board(board):
    print('-' * 13)
    for i in list(range(1, len(board) + 1)):
        print('| ' + str(board[i-1]), end=' ')
        if i % 3 == 0:
            print('|', end='')
            print()
            print('-' * 13)

def moves(board, player, how_many=2):
    sign = ''
    moves = list(range(1, 10))
    is_wrong = False
    if player == 1:
        sign = 'x'
    if player == 2:
        sign = 'o'
    if how_many == 2:
        move = int(input())
    else:
        if player == 1:
            move = int(input())
        if player == 2:
            move = choice(moves)
    if move in moves and board[move - 1] not in ['x', 'o']:
        board[move - 1] = sign
    else:
        is_wrong = True
        print("Invalid move. Choose another one!")

    return move, is_wrong

def main():
    p1_score = 0
    p2_score = 0
    print("How many players? ", end="")
    how_many = int(input())
    if how_many > 2 or how_many < 1:
        print("Invalid number of players. Choose between 1 or 2 player! " + \
              "(1 player you will play with the Computer).")
        return
    while True:
        print("Game is starting...")
        board = list(range(1, 10))
        list_of_moves = []
        player = 1
        print_board(board)
        while True:
            print()
            print("Player " + str(player) + ": Is your turn!")
            move, is_wrong = moves(board, player, how_many)
            print_board(board)
            if move in list_of_moves:
                continue
            else:
                list_of_moves.append(move)
            status = check_line(board, player)
            if status == 1 and len(list_of_moves) < 9:
                if player == 1 and not is_wrong:
                    player = 2
                else:
                    if player == 2 and not is_wrong:
                        player = 1
            else:
                if status == 0:
                    if player == 1:
                        p1_score += 1
                    else:
                        p2_score += 1
                    print("Player " + str(player) + " wins!")
                    print("Score: Player1 = ", p1_score)
                    print("Score: Player2 = ", p2_score)
                elif len(list_of_moves) == 9:
                    print("Draw!")

                game = input("Do you wanna play again? (Y for continuing, N for stopping): ")
                if game not in ['Y', 'N']:
                    print("Invalid argument!")
                    game = input("Do you wanna play again? (Y for continuing, N for stopping): ")
                if game == 'N':
                    print("Game Over")
                    return
                elif game == 'Y':
                    break 
                        

main()
