"""
Tic Tac Toe Player
"""

import math
import copy
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
    n_x,n_y=0,0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==X:
                n_x+=1
            elif board[i][j]==O:
                n_y+=1
    if n_x==n_y:
        return X
    elif n_x>n_y:
        return O
    raise NotImplementedError

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    s=set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                s.add((i, j))
    return s
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copyboard=copy.deepcopy(board)
    i,j=action
    if(copyboard[i][j]!=EMPTY):
        raise Exception("invalid action")
    else:
        copyboard[i][j]=player(board)
    return copyboard
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        firstnumber=board[i][0]
        if firstnumber!=EMPTY:
            secondnumber=board[i][1]
            if secondnumber==firstnumber:
                if board[i][2]==secondnumber:
                    return secondnumber
                else:
                    continue
            else:
                continue
        else:
            continue
    for i in range(3):
        firstnumber=board[0][i]
        if firstnumber!=EMPTY:
            secondnumber=board[1][i]
            if secondnumber==firstnumber:
                if board[2][i]==secondnumber:
                    return secondnumber
                else:
                    continue
            else:
                continue
        else:
            continue
    firstnumber=board[0][0]
    if firstnumber!= EMPTY:
        if board[1][1]==firstnumber:
            if board[2][2]==firstnumber:
                return firstnumber
    firstnumber=board[2][0]
    if firstnumber!= EMPTY:
        if board[1][1]==firstnumber:
            if board[0][2]==firstnumber:
                return firstnumber
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    non_empty_count=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False
            else:
                non_empty_count+=1
    if(non_empty_count==9):
        return True
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board)==X:
            return 1
        elif winner(board)==O:
            return -1
    return 0
    raise NotImplemenError

def max_val(board):
    if terminal(board):
        return utility(board)
    v=-1
    for i in actions(board):
        v=max(v, min_val(result(board,i)))
    return v

def min_val(board):
    if terminal(board):
        return utility(board)
    v=1
    for i in actions(board):
        v=min(v, max_val(result(board,i)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    act=list(actions(board))[0]
    if player(board)==X:
        val=-1
        for a in actions(board):
            minval=min_val(result(board, a))
            if minval>val:
                act=a
                val=minval
    if player(board)==O:
        val=1
        for a in actions(board):
            maxval=max_val(result(board, a))
            if maxval<val:
                act=a
                val=maxval

    return act

    raise NotImplementedError
