from tkinter import *

window = Tk()
window.title('Noughts and Crosses')
window.geometry('400x400')
window.resizable(0,0)

input_frame = Frame(window, width=300, height=300, bd=0, highlightbackground='black', highlightcolor='black', highlightthickness=1)
input_frame.pack(side=TOP)

class Square:
    def __init__(self, frame, posX, posY):
        self.frame = frame
        self.posX = posX
        self.posY = posY
        self.squareText = ''
        self.createSquare()
        
    def createSquare(self):
        self.square = Button(self.frame, text=self.squareText, width=10, height=5, bd=0, bg='#eee', cursor='hand2', command = lambda: self.playerMove(player))
        self.square.grid(row=self.posX, column=self.posY, padx=1, pady=1)
        
    def playerMove(self, player):
        self.squareText = player.value
        self.createSquare()
        print(self.squareText)

class Player:
    def __init__(self):
        self.value = 'X'
    def __repl__(self):
        return self.value


player = Player()

square1 = Square(input_frame, 0, 0)
square2 = Square(input_frame, 1, 1)
square3 = Square(input_frame, 2, 2)

window.mainloop()
