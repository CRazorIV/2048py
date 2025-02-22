import tkinter as tk
from tkinter import messagebox
from logic import Game2048
import random

CELL_COLORS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

CELL_NUMBER_COLORS = {
    0: "#cdc1b4",
    2: "#776e65",
    4: "#776e65",
    8: "#f9f6f2",
    16: "#f9f6f2",
    32: "#f9f6f2",
    64: "#f9f6f2",
    128: "#f9f6f2",
    256: "#f9f6f2",
    512: "#f9f6f2",
    1024: "#f9f6f2",
    2048: "#f9f6f2"
}

class Game2048GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048")
        self.window.config(bg="#faf8ef")
        self.window.resizable(False, False)

        # Game instance
        self.game = Game2048()
        
        # Create main frame
        self.main_frame = tk.Frame(
            self.window,
            bg="#faf8ef",
            padx=20,
            pady=20
        )
        self.main_frame.pack(expand=True, fill="both")

        # Score frame
        self.score_frame = tk.Frame(
            self.main_frame,
            bg="#faf8ef"
        )
        self.score_frame.pack(fill="x", pady=(0, 20))

        # Title
        self.title_label = tk.Label(
            self.score_frame,
            text="2048",
            font=("Helvetica", 48, "bold"),
            fg="#776e65",
            bg="#faf8ef"
        )
        self.title_label.pack(side="left")

        # Score
        self.score_label = tk.Label(
            self.score_frame,
            text="Score\n0",
            font=("Helvetica", 20),
            fg="#776e65",
            bg="#bbada0",
            width=8,
            padx=10,
            pady=5
        )
        self.score_label.pack(side="right")

        # Game grid
        self.cells = []
        self.create_board()

        # Bind keys
        self.window.bind("<Left>", lambda e: self.make_move("left"))
        self.window.bind("<Right>", lambda e: self.make_move("right"))
        self.window.bind("<Up>", lambda e: self.make_move("up"))
        self.window.bind("<Down>", lambda e: self.make_move("down"))

        # Center window
        self.window.update()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry(f"+{x}+{y}")

    def create_board(self):
        # Game board frame
        self.board_frame = tk.Frame(
            self.main_frame,
            bg="#bbada0",
            padx=10,
            pady=10
        )
        self.board_frame.pack()

        # Create cells
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.board_frame,
                    bg="#cdc1b4",
                    width=100,
                    height=100
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_frame.grid_propagate(False)
                
                cell_number = tk.Label(
                    cell_frame,
                    text="",
                    font=("Helvetica", 30, "bold"),
                    bg="#cdc1b4"
                )
                cell_number.place(relx=0.5, rely=0.5, anchor="center")
                row.append(cell_number)
            self.cells.append(row)
        
        self.update_board()

    def update_board(self):
        for i in range(4):
            for j in range(4):
                value = self.game.board[i][j]
                cell = self.cells[i][j]
                
                if value == 0:
                    cell.config(text="")
                else:
                    cell.config(text=str(value))
                
                cell.config(
                    bg=CELL_COLORS.get(value, "#ff0000"),
                    fg=CELL_NUMBER_COLORS.get(value, "#ffffff")
                )
                cell.master.config(bg=CELL_COLORS.get(value, "#ff0000"))

        self.score_label.config(text=f"Score\n{self.game.score}")

    def make_move(self, direction):
        if self.game.move(direction):
            self.update_board()
            
            if self.game.is_game_over():
                messagebox.showinfo("Game Over!", f"Game Over!\nFinal Score: {self.game.score}")
                self.restart_game()
            elif self.game.is_win():
                if messagebox.askyesno("Congratulations!", "You've reached 2048! Continue playing?"):
                    self.game.continue_game()
                else:
                    self.restart_game()

    def restart_game(self):
        self.game.reset()
        self.update_board()

if __name__ == "__main__":
    game_gui = Game2048GUI()
    game_gui.window.mainloop()
