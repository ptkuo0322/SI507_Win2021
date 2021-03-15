
# CONSTANTS
PLAYER_NAMES = ["Nobody", "X", "O"] 

def player_name(player_id):
    '''return the name of a player with a specified ID

    Looks up the name in the PLAYER_NAMES global list

    Parameters
    ----------
    player_id: int
        player's id, which is an index into PLAYER_NAMES

    Returns
    -------
    string
        the player's name

    '''
    return PLAYER_NAMES[player_id]

print(player_name(0))


board = [0, "X", 0,   # top row:    indices 0, 1, 2
        0, 0, 0,   # middle row: indices 3, 4, 5
        0, 0, 0]   # bottom row: indices 6, 7, 8
        
def display_board(board):
    board_to_show = "" # string that will display the board, starts empty
    for i in range(len(board)):
        if board[i] == 0: # 0 means unoccupied
            # displayed numbers are one greater than the board index
            board_to_show += str(i + 1) # display cell number
        else:
            board_to_show += player_name(board[i]) # display player's mark
        if (i + 1) % 3 == 0: # every 3 cells, start a new row
            board_to_show += "\n"
        else:
            board_to_show += " | " # within a row, divide the cells
    print()
    print(board_to_show)

print(board[1])