import tkinter as tk # ek built-in Python library hai jo GUI applications banane ke liye use hoti hai

CELL_SIZE = 40
ERASER_SIZE = 20
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()

        self.cells = []
        self.create_grid()

        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink', outline='pink')
        self.canvas.bind("<B1-Motion>", self.move_eraser)  # Bind Left Click + Motion

    def create_grid(self):
        rows = CANVAS_HEIGHT // CELL_SIZE
        cols = CANVAS_WIDTH // CELL_SIZE

        for i in range(rows):
            for j in range(cols):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='white')
                self.cells.append(cell)

    def move_eraser(self, event):
        # Move the eraser based on the mouse position
        x = event.x
        y = event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        
        # Erase cells that are overlapping with the eraser
        self.erase(x, y)

    def erase(self, x, y):
        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for obj in overlapping:
            if obj != self.eraser:
                self.canvas.itemconfig(obj, fill='white')  # Change the cell color to white

# Run the program
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ali Akbar's Eraser Canvas App")
    app = EraserApp(root)
    root.mainloop()
