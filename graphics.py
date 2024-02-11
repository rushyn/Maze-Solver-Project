from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, width = width, height = height, background="white")
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color="Black"):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        counter = 0
        while self.running is True:
            #print("running", counter)
            self.redraw()
            counter += 1
        print("window closed...")

    def close(self):
        self.running = False


class Point():
    def __init__(self, x, y):
        self.horizontal = x
        self.vertical = y


class Line():
    def __init__(self, p1, p2):
        self.x1 = p1.horizontal
        self.x2 = p2.horizontal
        self.y1 = p1.vertical
        self.y2 = p2.vertical
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
        canvas.pack()
