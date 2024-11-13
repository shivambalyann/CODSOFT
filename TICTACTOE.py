import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, root):  # Corrected constructor name
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Arial", 20), height=3, width=6,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.status_label = tk.Label(self.root, text="X's turn", font=("Arial", 15))
        self.status_label.grid(row=3, column=0, columnspan=3)

        restart_button = tk.Button(self.root, text="Restart", font=("Arial", 15),
                                   command=self.restart_game)
        restart_button.grid(row=4, column=0, columnspan=3)

    def on_button_click(self, index):
        if self.board[index] == " " and self.current_player == "X":
            self.make_move(index)
            if not self.check_end_game():
                self.current_player = "O"
                self.status_label.config(text="O's turn")
                self.root.after(500, self.ai_move)

    def make_move(self, index):
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

    def ai_move(self):
        move = self.best_move()
        self.make_move(move)
        if not self.check_end_game():
            self.current_player = "X"
            self.status_label.config(text="X's turn")

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def check_end_game(self):
        if self.check_winner("X"):
            self.end_game("X wins!")
            return True
        if self.check_winner("O"):
            self.end_game("O wins!")
            return True
        if " " not in self.board:
            self.end_game("It's a draw!")
            return True
        return False

    def end_game(self, result):
        messagebox.showinfo("Game Over", result)
        self.restart_game()

    def restart_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"
        self.status_label.config(text="X's turn")

    def minimax(self, is_maximizing):
        if self.check_winner("O"):
            return 1
        if self.check_winner("X"):
            return -1
        if " " not in self.board:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    move = i
        return move

if __name__ == "__main__":  # Corrected main block check
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
