"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
            
    return board_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    chance = player(board)
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = chance
    return new_board


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
    
    if winner(board=board):
        return True
    
    for i in board:
        for j in i:
            if j is None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    print("Board: ",board)
    for i in range(len(board)):
        if (board[i][0]==board[i][1]==board[i][2]==X or 
            board[0][i]==board[1][i]==board[2][i]==X):
            return 1
        elif (board[i][0]==board[i][1]==board[i][2]==O or 
              board[0][i]==board[1][i]==board[2][i]==O):
            return -1        
    # diagonals
    if (board[0][0]==board[1][1]==board[2][2]==X or 
        board[0][2]==board[1][1]==board[2][0]==X):
            return 1
    elif (board[0][0]==board[1][1]==board[2][2]==O or 
        board[0][2]==board[1][1]==board[2][0]==O):
            return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

def min_value(board):
    # If there is no other move possible the utility of the board is its min_value
    if terminal(board=board):
        return utility(board=board)
    
    action_set = actions(board=board)
    minima = 2
    for action in action_set:
        r = result(board=board, action=action)
        tertiary = max_value(board=r)
        if tertiary<minima:
            minima = tertiary
            
    return minima
            
def max_value(board):
    # If there is no other move possible the utility of the board is its max_value
    if terminal(board=board):
        return utility(board=board)
    
    action_set = actions(board=board)
    maxima = -2
    
    for action in action_set:
        r = result(board=board, action=action)
        tertiary = min_value(r)
        if tertiary>maxima:
            maxima = tertiary
    return maxima