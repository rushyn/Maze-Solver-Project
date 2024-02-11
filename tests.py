import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 25
        num_rows = 25
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 30
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_left_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows -1].has_right_wall,
            False,
        )
    
    def test_cels_visited_reset(self):
        num_cols = 13
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(m1.num_cols):
            for j in range(m1.num_rows):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()