from graphics import Window
from cell import Cell
from maze import Maze

def main():
    #win = Window(800, 600)
    #point1 = Point(100, 100)
    #point2 = Point(400, 400)
    #cell1 = Cell(Point(100, 100), Point(400, 400))
    
    #c1 = Cell(win)
    #c1.has_right_wall = False
    #c1.draw(50, 50, 100, 100)

    #c2 = Cell(win)
    #c2.has_left_wall = False
    #c2.has_bottom_wall = False
    #c2.draw(100, 50, 150, 100)

    #c1.draw_move(c2)

    #c3 = Cell(win)
    #c3.has_top_wall = False
    #c3.has_right_wall = False
    #c3.draw(100, 100, 150, 150)

    #c2.draw_move(c3)

    #c4 = Cell(win)
    #c4.has_left_wall = False
    #c4.draw(150, 100, 200, 150)

    #c3.draw_move(c4, True)

    #win.draw_line(cell1, "black")

    #m1 = Maze(20, 20, 5, 5, 50, 50, win)
    #m1._create_cells()
    #win.wait_for_close()

    num_rows = 15
    num_cols = 15
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, None)

    win.wait_for_close()



main()
