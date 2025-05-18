"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    a = 0
    b = 0
    
    for i in board:
        for j in i:
            if j == X:
                a+=1
            elif j == O:
                b+=1
    if a==b:
        return X
    return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    board_actions = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==None:
                board_actions.append((i,j))
            
    return set(board_actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    chance = player(board)
    board[action[0], action[1]] = chance
    return board


def winner(board):
    """
    Returns the winner of the game if there is one
    """
    
    for i in range(len(board)):
        if board[i][0]==board[i][1]==board[i][2]!=None:
            return board[i][0]
        elif board[0][i]==board[1][i]==board[2][i]!=None:
            return board[0][i]
        
    # diagonals
    if board[0][0]==board[1][1]==board[2][2]!=None:
            return board[0][0]
        
    if board[0][2]==board[1][1]==board[2][0]!=None:
            return board[0][2]
        
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
