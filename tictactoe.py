'''
The Tic-Tac_Toe game for two players, X and O, who take turns marking
the spaces in a 3×3 grid. The player who succeeds in placing three of
their marks in a horizontal, vertical, or diagonal row is the winner.

After starting the game, an empty playing field and a line appear in
front of you, inviting you to enter coordinates. Player H moves first,
he must select an empty cell on the playing field by entering
coordinates in the x y format, where each coordinate must be in the
range from 1 to 3.

The layout of the field starts from the lower left corner,
which has coordinates 1 1, lower right the corner has coordinates 3 1.

Let's play, good luck to the players.

'''

def print_field():
    print("---------")
    for row in field:
        print("|", *row, "|")
    print("---------")


def player_change(*a):
    if "X" in a:
        return "O"
    else:
        return "X"

def check_users_coordinate(s):
    s = s.split()
    for i in s:
        # enters other symbols
        if not i.isdigit() or len(s) < 2:
            return "You should enter numbers!"
        # goes beyond the field
        if int(i) > 3 or int(i) < 1:
            return "Coordinates should be from 1 to 3!"
    # the cell is not empty
    x, y = (int(i) for i in s)
    if field[3 - y][x - 1] != " ":
        return "This cell is occupied! Choose another one!"


def analize_field():
    o_cnt = 0
    o_win = False
    x_cnt = 0
    x_win = False
    _cnt = 0

    # Impossible case
    # the number of moves of one of the players is much more than the other
    for line in field:
        for cell in line:
            if cell == "X":
                x_cnt += 1
            elif cell == "O":
                o_cnt += 1
            else:
                _cnt += 1
    if abs(o_cnt - x_cnt) > 1:
        return "Impossible"

    # searching of winner
    # line in row
    for line in field:
        if line[0] == line[1] == line[2]:
            if line[0] == "X":
                x_win = True
            if line[0] == "O":
                o_win = True
    # line in column
    for i in (0, 1, 2):
        if field[0][i] == field[1][i] == field[2][i]:
            if field[0][i] == "X":
                x_win = True
            elif field[0][i] == "O":
                o_win = True
    # line by diagonal
    for i in (0, 1, 2):
        if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
            if field[1][1] == "X":
                x_win = True
            elif field[1][1] == "O":
                o_win = True
    if x_win == o_win != 0:
        return "Impossible"
    elif x_win:
        return "X wins"
    elif o_win:
        return "O wins"
    # Draw case
    if _cnt == 0:
        return "Draw"
    return "Game not finished"


# create empty game field
field = [[" " for _ in range(3)] for _ in range(3)]

# game field printing
print_field()
player = ''
# game loop
while analize_field() == "Game not finished":
    player = player_change(player)
    print("Player {}'s turn".format(player))
    while True:
        player_mov = input("Enter the coordinates: > ")
        checking = check_users_coordinate(player_mov)
        print(checking)
        if not checking:
            break
    x, y = (int(i) for i in player_mov.split())
    field[3 - y][x - 1] = player
    print_field()
else:
    print(analize_field())





