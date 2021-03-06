"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str, riv: str) -> list[int, int]:
    """
    Decides next move to make.
    """
    
    A = board[0][0]
    B = board[0][1]
    C = board[0][2]

    D = board[1][0]
    E = board[1][1]
    F = board[1][2]

    G = board[2][0]
    H = board[2][1]
    I = board[2][2]

    # Start
    if A == "-" and B == "-" and C == "-" and D == "-" and E == "-" and F == "-" and G == "-" and H == "-" and I =="-":
       
        a = randint(0, 1)

        if a == 1:
            return [1, 2]

        if a == 0:
            return [0, 1]
    
    # Possible ways to win
    if E == player_id and D == "-" and F == player_id or D == "-" and A == player_id and G == player_id:
        return [1, 0]
    
    if A == "-" and B == player_id and C == player_id or A == "-" and D == player_id and G == player_id or A == "-" and E == player_id and I == player_id:
        return [0, 0]

    if A == player_id and B == player_id and C == "-" or  E == player_id and G == player_id and C == "-" or I == player_id and F == player_id and C == "-":
        return [0, 2]
    
    if  H == player_id and E == player_id and B == "-" or A == player_id and C == player_id and B == "-":
        return [0, 1]
    
    if D == player_id and E == "-" and F == player_id or B == player_id and E == "-" and H == player_id or A == player_id and E == "-" and I == player_id or C == player_id and E == "-" and G == player_id:
        return [1, 1]
    
    if  D == player_id and E == player_id and F == "-" or E == player_id and F == "-" and I == player_id:
        return [1, 2]

    if C == player_id and E == player_id and G == "-" or A == player_id and D == player_id and G == "-" or I == player_id and H == player_id and G == "-":
        return [2, 0]
    
    if G == player_id and I == player_id and H == "-" or B == player_id and D == player_id and H == "-":
        return [2, 1]
    
    if I == "-" and H == player_id and G == player_id or I == "-" and C == player_id and F == player_id or I == "-" and C == player_id and F == player_id:
        return [2, 2]

    

    # Defense start
    if A == riv and B == "-" and C == "-" and D == "-" and E == "-" and F == "-" and G == "-" and H == "-" and I =="-"or A == "-" and B == riv and C == "-" and D == "-" and E == "-" and F == "-" and G == "-" and H == "-" and I =="-" or A == "-" and B == "-" and C == riv and D == "-" and E == "-" and F == "-" and G == "-" and H == "-" and I =="-" or A == "-" and B == "-" and C == "-" and D == riv and E == "-" and F == "-" and G == "-" and H == "-" and I =="-" or A == "-" and B == "-" and C == "-" and D == "-" and E == "-" and F == riv and G == "-" and H == "-" and I =="-" or A == "-" and B == "-" and C == "-" and D == "-" and E == "-" and F == "-" and G == riv and H == "-" and I =="-" or A == "-" and B == "-" and C == "-" and D == "-" and E == "-" and F == "-" and G == "-" and H == riv and I =="-" or A == "-" and B == "-" and C == "-" and D == "-" and E == "-" and F == "-" and G == "-" and H == "-" and I == riv:
        return [1, 1]
    
    if A == "-" and B == "-" and C == "-" and D == "-" and E == riv and F == "-" and G == "-" and H == "-" and I =="-":
        return [2, 2]



    # Defense tactic
    if A == "-" and B == riv and C == riv or A == "-" and D == riv and G == riv or A == "-" and E == riv and I == riv:
        return [0, 0]
    
    if A == riv and B == riv and C == "-" or E == riv and G == riv and C == "-" or I == riv and F == riv and C == "-":
        return [0, 2]

    if D == riv and E == riv and F == "-" or E == riv and F == "-" and I == riv:
        return [1, 2]

    if D == "-" and E == riv and F == riv or D == "-" and A == riv and G == riv:
        return [1, 0]
    
    if D == riv and E == "-" and F == riv or B == riv and E == "-" and H == riv or A == riv and E == "-" and I == riv or C == riv and E == "-" and G == riv:
        return [1, 1]
    
    if I == "-" and H == riv and G == riv or I == "-" and C == riv and F == riv or I == "-" and E == riv and A == riv:
        return [2, 2]
    
    if H == riv and E == riv and B == "-" or A == riv and C == riv and B == "-":
        return [0, 1]
     
    if C == riv and E == riv and G == "-" or A == riv and D == riv and G == "-" or I == riv and H == riv and G == "-":
        return [2, 0]
    
    if  G == riv and I == riv and H == "-" or B == riv and D == riv and H == "-":
        return [2, 1]



    # Opening tactic 1.0
    if F == player_id and E == "-":
        return [1, 1]
    
    if F == player_id and E == player_id and D == "-":
        return [1, 0]
    
    if F == player_id and E == player_id and C == "-":
        return [0, 2]
    
    if F == player_id and C == player_id and I == "-":
        return [2, 2]
    
    if C == player_id and E == player_id and G == "-":
        return [2, 0]
    


    # Opening tactic 1.1
    if F == player_id and E == riv and I =="-":
        return [2, 2]
    
    if F == player_id and I == player_id and C == "-":
        return [0, 2]



    # Opening tactic 2.0
    if B == player_id and C == "-":
        return [0, 2]

    if B == player_id and C == player_id and A == "-":
        return [0, 0]

    if B == player_id and C == player_id and E == "-":
        return [1, 1]

    if B == player_id and E == player_id and H == "-":
        return [2, 1]

    if C == player_id and E == player_id and G == "-":
        return [2, 0]


    
    else:
        row = randint(0, 2)
        column = randint(0, 2)
        return [row, column]


def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")
