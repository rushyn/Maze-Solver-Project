import time, random
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells        = []
        self._x1           = x1
        self._y1           = y1
        self.num_rows      = num_rows
        self.num_cols      = num_cols
        self.cell_size_x   = cell_size_x
        self.cell_size_y   = cell_size_y
        self._win          = win
        if seed is not None:
            random.seed(seed)
        self._create_cells() 
        self._break_entrance_and_exit()
        self.break_wall_r(0, 0)
        self._reset_cells_visited()
        self.solve()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for i in range(self.num_rows)] for j in range(self.num_cols)]
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x = self._x1 + (i * self.cell_size_x)
        cell_y = self._y1 + (j * self.cell_size_y)
        self._cells[i][j].draw(cell_x, cell_y, cell_x + self.cell_size_x, cell_y + self.cell_size_y)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        
    def break_wall_r(self, ii, jj):
        self._cells[ii][jj].visited = True
        while True:
            cell_pos = list()
            for i in range(ii - 1, ii + 2):
                for j in range(jj - 1, jj + 2):
                    if i >= 0 and j >= 0 and i < self.num_cols and j < self.num_rows:
                        #print("yay1", i, j)
                        if self._cells[i][j].visited == False:
                            #print("yay2")
                            if i == ii or j == jj:
                                #print("yay3")
                                cell_pos.append([i, j])
            #print("cell_pos", cell_pos)
            if len(cell_pos) == 0:
                return
            go_to = cell_pos[random.randrange(len(cell_pos))]
            #print(ii, jj, "go_to", go_to)
            if go_to[0] < ii:
                #print("left")
                self._cells[ii][jj].has_left_wall = False
                self._cells[go_to[0]][go_to[1]].has_right_wall  = False
            elif go_to[0] > ii:
                #print("right")
                self._cells[ii][jj].has_right_wall  = False
                self._cells[go_to[0]][go_to[1]].has_left_wall = False
            elif go_to[1] < jj:
                #print("up")
                self._cells[ii][jj].has_top_wall  = False
                self._cells[go_to[0]][go_to[1]].has_bottom_wall  = False
            else:
                #print("down")
                self._cells[ii][jj].has_bottom_wall  = False
                self._cells[go_to[0]][go_to[1]].has_top_wall  = False
            #print(ii, jj)
            self._draw_cell(ii, jj)
            #time.sleep(1.5)
            #print(go_to[0], go_to[1])
            self._draw_cell(go_to[0], go_to[1])
            #time.sleep(1.5)
            self.break_wall_r(go_to[0], go_to[1])
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        return self._solver_r(0, 0)
    
    def _solver_r(self, ii, jj):
        self._animate()
        self._cells[ii][jj].visited = True
        if ii == self.num_cols - 1 and jj == self.num_rows - 1:
            return True
        for i in range(ii - 1, ii + 2):
            for j in range(jj - 1, jj + 2):
                if i >= 0 and j >= 0 and i < self.num_cols and j < self.num_rows:
                    if self._cells[i][j].visited == False:
                        if i == ii or j == jj:
                            #print(ii, jj, "move to", i, j)
                            if i < ii:
                                if self._cells[ii][jj].has_left_wall == False:
                                    if self._cells[i][j].has_right_wall  == False:
                                        self._cells[i][j].draw_move(self._cells[ii][jj])
                                        if self._solver_r(i, j) is True:
                                            return True
                                        else:
                                            self._cells[ii][jj].draw_move(self._cells[i][j], True)
                            if i > ii:
                                if self._cells[ii][jj].has_right_wall  == False:
                                    if self._cells[i][j].has_left_wall == False:
                                        self._cells[i][j].draw_move(self._cells[ii][jj])
                                        if self._solver_r(i, j) is True:
                                            return True
                                        else:
                                            self._cells[ii][jj].draw_move(self._cells[i][j], True)
                            if j < jj:
                                if self._cells[ii][jj].has_top_wall  == False:
                                    if self._cells[i][j].has_bottom_wall  == False:
                                        self._cells[i][j].draw_move(self._cells[ii][jj])
                                        if self._solver_r(i, j) is True:
                                            return True
                                        else:
                                            self._cells[ii][jj].draw_move(self._cells[i][j], True)
                            if j > jj:
                                if self._cells[ii][jj].has_bottom_wall  == False:
                                    if self._cells[i][j].has_top_wall  == False:
                                        self._cells[i][j].draw_move(self._cells[ii][jj])
                                        if self._solver_r(i, j) is True:
                                            return True
                                        else:
                                            self._cells[ii][jj].draw_move(self._cells[i][j], True)
        return False
