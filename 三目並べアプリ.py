import tkinter as tk

class order_three_dimention(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.OPEN = 0
        self.FIRST = 1
        self.SECOND = -1
        self.DRAW = 3
        self.turn = 1
        self.board = [[0,0,0], [0,0,0],[0,0,0]]
        self.buttons_status = [True]*9
        
        self.b1 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(1))
        self.b2 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(2))
        self.b3 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(3))
        self.b4 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(4))
        self.b5 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(5))
        self.b6 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(6))
        self.b7 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(7))
        self.b8 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(8))
        self.b9 = tk.Button(self, text='', width=12, height=7, font=('', 13, 'bold'), command=lambda:self.toggle(9))
        self.br = tk.Button(self, text='Restart', width=12, height=3, command=self.restart)
    
        self.b1.grid(row=1, column=0, pady=(0,0))
        self.b2.grid(row=1, column=1, pady=(0,0))
        self.b3.grid(row=1, column=2, pady=(0,0))
        self.b4.grid(row=2, column=0, pady=(0,0))
        self.b5.grid(row=2, column=1, pady=(0,0))
        self.b6.grid(row=2, column=2, pady=(0,0))
        self.b7.grid(row=3, column=0)
        self.b8.grid(row=3, column=1)
        self.b9.grid(row=3, column=2)
        self.br.grid(row=5, column=0)
        
        self.button_status = True
        self.buttons = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        
        self.e = tk.Entry(self, width=21, font=('', 25))
        self.e.insert(0, 'FIRST TURN')
        self.e.grid(row=0, column=0, columnspan=3)
        
    def init_board(self):
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
    
    def toggle(self, k):
        for i in range(9):
            if k == i+1:
                if self.buttons_status[i]:
                    if self.turn == self.FIRST:
                        self.buttons[i].configure(text='O')
                        self.board[i//3][i%3] = self.turn
                        self.buttons_status[i] = False
                        self.show_turn('SECOND')
                        print(self.board)                        
                    elif self.turn == self.SECOND:
                        self.buttons[i].configure(text='X')
                        self.board[(k-1)//3][(k-1)%3] = self.turn
                        self.buttons_status[i] = False
                        self.show_turn('FIRST')
                        print(self.board)
                else:
                    self.show_error('not empty')
            else:
                'k is out of range'
        if self.simple_win(self.turn):
            if self.turn == self.FIRST:
                self.show_winner('FIRST')
            elif self.turn == self.SECOND:
                self.show_winner('SECOND')
            for i in range(9):
                self.buttons_status[i] = False
        elif not self.check_full():
            self.show_winner('NEITHER')
            
            
                
        self.turn *= -1
        
    def init_buttons(self):
        for i in range(9):
            self.buttons[i].configure(text='')
            self.buttons_status[i] = True
            
    def show_turn(self, turn):
        self.e.delete(0, 'end')
        self.e.insert(0, f'{turn} TURN')
        
    def check_board_horizontal(self, t):
        for i in range(3):
            if (self.board[i][0] == t) and (self.board[i][1] == t) and (self.board[i][2] == t):
                return True
        
    def check_board_vertical(self, t):
        for j in range(3):
            if (self.board[0][j] == t) and (self.board[1][j] == t) and (self.board[2][j] == t):
                return True
    
    def check_board_diagonal(self, t):
        if (self.board[0][0] == t) and (self.board[1][1] == t) and (self.board[2][2] == t):
            return True
    
    def check_board_inverse_diagonal(self, t):
        if (self.board[0][2] == t) and (self.board[1][1] == t) and (self.board[2][0] == t):
            return True
    
    def simple_win(self, t):
        if self.check_board_horizontal(t):
            return True
        elif self.check_board_vertical(t):
            return True
        elif self.check_board_diagonal(t):
            return True
        elif self.check_board_inverse_diagonal(t):
            return True
        return False
    
    def show_winner(self, turn):
        self.e.delete(0, 'end')
        self.e.insert(0, f'{turn} WIN!! ')
        
    def show_error(self, k):
        self.e.delete(0, 'end')
        self.e.insert(0, f'{k}')
        
    def restart(self):
        self.init_board()
        self.init_buttons()
        self.turn = 1
        self.show_turn('FIRST')
    
    def check_full(self):
        for i in range(9):
            if self.buttons_status[i]:
                return True
        return False
    
    
root = tk.Tk()
frame = order_three_dimention(root)
frame.pack()
root.mainloop()


        
        
    