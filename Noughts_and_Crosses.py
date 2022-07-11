"""
In this question you need to implement an optimal player for the game noughts and crosses (aka Tic-tac-toe). We generalise the game to an n-by-n board where a 
player wins if some of their pieces form a complete row, column, or one of the two diagonals. We represent the board by a list of lists (list of rows) where 
the elements are either X, O, or '.'.

Write a function optimal_move(board, player) that takes a board and a player (characters 'X' or 'O') and returns a pair (row, col) where the player must 
place her next piece in order to guarantee the best possible result. If multiple moves are equally good, the function must return one that has the lowest 
row number and then the lowest column number. The function will be tested with various board sizes (n larger than zero). The size of the search space will 
be roughly about that of an empty board with n=3. The function must compute the optimal move in less than a second.

Notes
Since we are using a mutable object (list of lists) to represent the board, make sure the board does not get accidentally modified in your function.
You are required to submit only one function. Other functions you see in the test cases are defined on the server (but not accessible by your code). It is 
up to you how you decompose the problem into several functions (or take an OO approach).
You will need to do pruning in order to meet the required time constraint.
If allocating and deallocating memory (creating new boards in each stack frame) is slowing down your program, you can keep track moves in stack frames and 
work with only one board (i.e. move, make the recursive call, and then 'unmove' all on the same board).
It is recommended that you do some local testing with some games before submitting your solution.
"""


def optimal_move(board, player):
    n = len(board)
    if player == 'X':
        
    else:
        
    return


def main():
    board = [['.', '.'], ['.', '.']]
    player = 'X'
    
    print(optimal_move(board, player))
    
    
    board_str = """\
    ...
    ...
    ...
    """
    
    board = board_from_string(board_str)
    player = student = 'X'
    
    display(board)
    while not is_terminal(board):
        move_function = student_optimal if player == student else server_optimal
        move = move_function(board, player)
        print(f"{player} plays {move}:")
        apply(move, board, player)
        display(board)
        player = opponent(player)
        
if __name__ == '__main__':
    main()