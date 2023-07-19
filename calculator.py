import tkinter as tk


class MyFrame(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.current_number = 0
        self.operation = '+'
        
        b1 = tk.Button(self, text='1', width=10, height=5, command=lambda:self.key(1))
        b2 = tk.Button(self, text='2', width=10, height=5, command=lambda:self.key(2))
        b3 = tk.Button(self, text='3', width=10, height=5, command=lambda:self.key(3))
        b4 = tk.Button(self, text='4', width=10, height=5, command=lambda:self.key(4))
        b5 = tk.Button(self, text='5', width=10, height=5, command=lambda:self.key(5))
        b6 = tk.Button(self, text='6', width=10, height=5, command=lambda:self.key(6))
        b7 = tk.Button(self, text='7', width=10, height=5, command=lambda:self.key(7))
        b8 = tk.Button(self, text='8', width=10, height=5, command=lambda:self.key(8))
        b9 = tk.Button(self, text='9', width=10, height=5, command=lambda:self.key(9))
        b0 = tk.Button(self, text='0', width=10, height=5, command=lambda:self.key(0))
        be = tk.Button(self, text='=', width=10, height=5, command=self.eq, bg = 'silver')
        bp = tk.Button(self, text='+', width=10, height=5, command=self.plus, bg = 'silver')
        bs = tk.Button(self, text='-', width=10, height=5, command=self.minus, bg = 'silver')
        bm = tk.Button(self, text='×', width=10, height=5, command=self.multiple, bg = 'silver')
        bd = tk.Button(self, text='%', width=10, height=5, command=self.divide, bg = 'silver')
        bc = tk.Button(self, text='C', width=10, height=5, command=self.clear, bg = 'red')
        
        b1.grid(row=3, column=0)
        b2.grid(row=3, column=1)
        b3.grid(row=3, column=2)
        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)
        b7.grid(row=1, column=0)
        b8.grid(row=1, column=1)
        b9.grid(row=1, column=2)
        b0.grid(row=4, column=0)
        be.grid(row=1, column=3)
        bc.grid(row=1, column=4)
        bp.grid(row=3, column=3)
        bs.grid(row=4, column=3)
        bm.grid(row=3, column=4)
        bd.grid(row=4, column=4)
        
        
        self.e = tk.Entry(self,width=35, font=('', 15))
        self.e.grid(row=0, column=0, columnspan=5)
        
    def key(self, n):
        self.current_number = self.current_number*10 + n
        self.show_number(self.current_number)
    
    def clear(self):
        self.current_number = 0
        self.show_number(self.current_number)
        self.result = 0
        self.first_term = 0
        self.second_term = 0
        self.current_number = 0
        
    def plus(self):
        self.operation = '+'
        self.first_term = self.current_number
        self.current_number = 0
     
    def minus(self):
        self.operation = '-'
        self.first_term = self.current_number
        self.current_number = 0
    
    def multiple(self):
        self.operation = '*'
        self.first_term = self.current_number
        self.current_number = 0
    
    def divide(self):
        self.operation = '/'
        self.first_term = self.current_number
        self.current_number = 0
        
    def eq(self):
        self.second_term = self.current_number
        if self.operation == '+':
            self.result = self.first_term + self.second_term
        if self.operation == '-':
            self.result = self.first_term - self.second_term
        if self.operation == '*':
            self.result = self.first_term * self.second_term
        if self.operation == '/':
            self.result = self.first_term / self.second_term
        self.show_number(self.result)
        self.current_number = self.result
        self.first_term = 0
        self.second_term = 0
        
    def show_number(self, num):
        self.e.delete(0, tk.END)
        self.e.insert(0, str(num))
        
root = tk.Tk()
f = MyFrame(root)
f.pack()
root.mainloop()
    
    
    
    
    
    
    
    
