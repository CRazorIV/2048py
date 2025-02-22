import random

class Game2048:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.won = False
        # Add two initial tiles
        self.add_new_tile()
        self.add_new_tile()
        
    def add_new_tile(self):
        empty_cells = [
            (i, j) for i in range(4) 
            for j in range(4) if self.board[i][j] == 0
        ]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4
            
    def move(self, direction):
        # Store the current board state
        old_board = [row[:] for row in self.board]
        
        if direction == "left":
            self.move_left()
        elif direction == "right":
            self.reverse_board()
            self.move_left()
            self.reverse_board()
        elif direction == "up":
            self.transpose_board()
            self.move_left()
            self.transpose_board()
        elif direction == "down":
            self.transpose_board()
            self.reverse_board()
            self.move_left()
            self.reverse_board()
            self.transpose_board()
            
        # Check if the board changed
        changed = any(
            old_board[i][j] != self.board[i][j]
            for i in range(4) for j in range(4)
        )
        
        if changed:
            self.add_new_tile()
            
        return changed
            
    def move_left(self):
        for i in range(4):
            # Merge tiles
            line = [x for x in self.board[i] if x != 0]
            for j in range(len(line) - 1):
                if line[j] == line[j + 1]:
                    line[j] *= 2
                    line[j + 1] = 0
                    self.score += line[j]
                    if line[j] == 2048:
                        self.won = True
                        
            # Remove zeros and pad with zeros
            line = [x for x in line if x != 0]
            line.extend([0] * (4 - len(line)))
            self.board[i] = line
            
    def reverse_board(self):
        for i in range(4):
            self.board[i].reverse()
            
    def transpose_board(self):
        self.board = list(map(list, zip(*self.board)))
        
    def is_game_over(self):
        # Check for empty cells
        if any(0 in row for row in self.board):
            return False
            
        # Check for possible merges
        for i in range(4):
            for j in range(4):
                current = self.board[i][j]
                # Check right neighbor
                if j < 3 and current == self.board[i][j + 1]:
                    return False
                # Check bottom neighbor
                if i < 3 and current == self.board[i + 1][j]:
                    return False
                    
        return True
        
    def is_win(self):
        return self.won
        
    def continue_game(self):
        self.won = False
