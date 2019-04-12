'''
Author: Bryan Ward
purpose: Minesweeper
the chronicles of my life it all started when...
'''
from graphics import *
from time import clock
from random import seed, randint
from re import split

TILE_IMAGE = 'tile.gif'
FLAG_IMAGE = 'flag.gif'
MINE_IMAGE = 'mine.gif'
LOSE_IMAGE = 'lose.gif'
SMILEY_IMAGE = 'smiley.gif'
BLANK_CELL = 0
EXPOSED_CELL = 10
MINE_CELL = 13
MAX_ADJACENT_MINES = 8


WIDTH_OF_IMAGES = 32
HEIGHT_OF_IMAGES = 32


LEFT_OFFSET = 100
RIGHT_OFFSET = 100
TOP_OFFSET = 120
BOTTOM_OFFSET = LEFT_OFFSET // 2


X_OFFSET = LEFT_OFFSET
Y_OFFSET = TOP_OFFSET

window = GraphWin('Color Canvas', 1100, 1000, autoflush=False )


def create_minesweeper_matrix(rows, columns):
    """

    :param rows:
    :param columns:
    :return: arary
    """

    mine_sweeper_array = []            # create an empty list
    for i in range(rows):
        mine_sweeper_array.append([])  # append an empty list to mine_sweeper_array
        for j in range(columns):
            mine_sweeper_array[i].append(0)   # mine_sweeper_array[i] is the empty list that we just created.
                                 # here, we are adding elements to it.
    return mine_sweeper_array






def print_game_board(game_board_marker):



    for i in range(len(game_board_marker)):
        for j in range(len(game_board_marker[i])):
            print(str(game_board_marker[i][j]).rjust(2), ' ', end='')
        print()









    return game_board_marker



def populate_with_mines(game_board_markers, number_of_mines):

    """
    All cells of the game_board_markers that is passed to the following function contain zeros.
    This function randomly selects number_of_mines cells of this two dimensional array and designates
    them as mine-cells. On return, number_of_mines cells of game_board_markers will contain MINE_CELL.

    :param game_board_marker:
    :return:
    """
    count = 0


    while count < number_of_mines:


        mine_in_row = randint(0,len(game_board_markers )-1)
        mine_in_columns = randint(0,len(game_board_markers[0]) - 1)




        if game_board_markers[mine_in_row][mine_in_columns] != MINE_CELL:

            game_board_markers[mine_in_row][mine_in_columns] = MINE_CELL



            count += 1





    return

def update_neighbor_count(game_board_markers, row, column):
    '''

    :param game_board_markers:
    :param row:
    :param column:
    :return:
    '''


    count = 0
    for i in [-1,0,1]:

        for j in [-1,0,1]:

            if 0 <= row + i<= len(game_board_markers)-1 and 0 <= column + j <= len(game_board_markers[0])-1 and game_board_markers[row+i][column+j] == MINE_CELL:

                count += 1
    if game_board_markers[row][column] >= MINE_CELL:

        count = MINE_CELL
    return count


def add_mine_counts(game_board_markers):
    '''

    :param game_board_markers:
    :return:
    '''
    for i in range(len(game_board_markers)):
        for j in range(len(game_board_markers[i])):
            game_board_markers[i][j] = update_neighbor_count(game_board_markers, i, j)


def draw_the_grid(rows, columns, win):
    '''

    :param rows:
    :param columns:
    :param win:
    :return:
    '''
    blank_grid_list = []
    for i in range(rows):

        y_grid = Y_OFFSET + HEIGHT_OF_IMAGES * i
        blank_grid_list.append([])


        for j in range(columns):
            x_grid = X_OFFSET + WIDTH_OF_IMAGES * j

            first_grid_point = Point(x_grid,y_grid)
            second_point = Point(x_grid + WIDTH_OF_IMAGES,y_grid + HEIGHT_OF_IMAGES )
            mine_grid = Rectangle(first_grid_point,second_point)
            mine_grid.draw(window)
            blank_grid_list[i].append(mine_grid)

    return blank_grid_list

def draw_board_numbers(game_board_markers, win, list):

    for i in range(len(game_board_markers[0])):
        text_y = Text(Point(X_OFFSET + WIDTH_OF_IMAGES/2 + WIDTH_OF_IMAGES * i ,Y_OFFSET - HEIGHT_OF_IMAGES/2),i)
        text_y.draw(window)

    for j in range(len(game_board_markers)):
        text_x = Text(Point(X_OFFSET - WIDTH_OF_IMAGES/2, Y_OFFSET + HEIGHT_OF_IMAGES/2 + HEIGHT_OF_IMAGES * j),j)
        text_x.draw(window)

    for i in range(len(game_board_markers)):
        for j in range(len(game_board_markers[0])):
            if game_board_markers[i][j] == MINE_CELL:
                square = list[i][j].getP1()
                Ypoint = square.getY() + HEIGHT_OF_IMAGES/2
                Xpoint = square.getX() + WIDTH_OF_IMAGES/2
                mine_image = Image(Point(Xpoint,Ypoint),MINE_IMAGE)
                mine_image.draw(window)
            elif 0 < game_board_markers[i][j] <= 8:
                point = list[i][j].getP1()
                Xpoint = point.getX() + WIDTH_OF_IMAGES/2
                Ypoint = point.getY() + HEIGHT_OF_IMAGES/2
                text = Text(Point(Xpoint,Ypoint), str(game_board_markers[i][j]))
                text.draw(win)



    










def main():




    level = input("Please select dificulty Beginner, Intermediate ,and Expert: ")

    if level == ('beginner') or level == ('1'):
        # Beginner game
        rows = 9
        columns = 9
        num_mines = 10

    elif level == ('intermediate') or level == ('2'):

        # Intermediate
        rows = 16
        columns = rows
        num_mines = 40


    elif level== ('expert') or level == ('3'):
        # Expert
        rows = 16
        columns = 30
        num_mines = 99

    game_board_markers = create_minesweeper_matrix(rows, columns)



    populate_with_mines(game_board_markers, num_mines)

    add_mine_counts(game_board_markers)

    print_game_board(game_board_markers)

    grid_list = draw_the_grid(rows,columns,window)

    draw_board_numbers(game_board_markers,window,grid_list)

    window.getMouse()


    window.close()




main()



