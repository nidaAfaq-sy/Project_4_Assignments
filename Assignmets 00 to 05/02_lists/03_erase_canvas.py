import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        self.cells = []
        self.create_grid()
        
        self.eraser = None
        self.canvas.bind("<Button-1>", self.create_eraser)  # Left-click to create eraser
        self.canvas.bind("<Motion>", self.move_eraser)  # Move eraser with mouse

    def create_grid(self):
        """Creates a grid of blue cells"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")
                self.cells.append(cell)  # Store cell references

    def create_eraser(self, event):
        """Creates the eraser at the mouse click position"""
        if self.eraser is None:
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE, fill="pink"
            )

    def move_eraser(self, event):
        """Moves the eraser with the mouse and erases blue squares"""
        if self.eraser:
            self.canvas.coords(self.eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
            self.erase_objects(event.x, event.y)

    def erase_objects(self, x, y):
        """Erases (turns white) any overlapping blue squares"""
        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for obj in overlapping:
            if obj in self.cells:
                self.canvas.itemconfig(obj, fill="white")  # Change to white instead of deleting

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()
