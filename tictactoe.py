#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9

from random import choice

board = list(range(1, 10))

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
    print("How many players? ", end="")
    how_many = int(input())
    print_board(board)
    while True:
        list_of_moves = []
        player = 1
        while True:
            print()
            print("Player " + str(player) + ": Is your turn!")
            move, is_wrong = moves(board, player, how_many)
            if move in list_of_moves:
                continue
            else:
                list_of_moves.append(move)
            status = check_line(board, player)
            print_board(board)
            if status == 1 and len(list_of_moves) < 9:
                if player == 1 and not is_wrong:
                    player = 2
                else:
                    if player == 2 and not is_wrong:
                        player = 1
            else:
                if status == 0:
                    print("Player " + str(player) + " wins!")
                    return
                if len(list_of_moves) == 9:
                    print("Draw!")
                    return

main()
