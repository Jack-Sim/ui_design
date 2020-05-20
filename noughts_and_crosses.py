from tkinter import *
import tkinter.font as font
import numpy as np

window = Tk()
window.title('Noughts and Crosses')
window.geometry('400x400')
window.resizable(0,0)

game_font = font.Font(family = 'arial', size = 30, weight = 'bold')

input_frame = Frame(window, width=300, height=300, bd=0, highlightbackground='black', highlightcolor='black', highlightthickness=1)
input_frame.pack(side=TOP)

class Square:
    def __init__(self, frame, posX, posY, id_no, game_font):
        self.frame = frame
        self.id = id_no
        self.posX = posX
        self.posY = posY
        self.font = game_font
        self.squareText = ''
        self.change = True
        self.createSquare()

    def __repr__(self):
        return str(self.id)

    def createSquare(self):
        self.square = Button(self.frame, text=self.squareText, width=4, height=2, bd=0, bg='#eee', cursor='hand2', command = lambda: self.playerMove(player))
        self.square['font'] = self.font
        self.square.grid(row=self.posX, column=self.posY, padx=1, pady=1)
        
    def playerMove(self, player):
        if self.change:
            self.squareText = player.value
            self.createSquare()
            game.checkBoard()
            player.changeValue()
            self.change = False
            
        else:
            pass
        
    def getSquareValue(self):
        return self.squareText

class Player:
    def __init__(self):
        self.value = 'X'
        self.text = StringVar()
        self.text.set(f'The current player is: {self.value}')
        self.whos_move = Label(window, textvariable = self.text)
        self.whos_move['font'] = font.Font(family='arial', size=18)
        self.whos_move.pack()
        
    def __repr__(self):
        return self.value
    
    def changeValue(self):
        if self.value == 'X':
            self.value = '0'
        elif self.value == '0':
            self.value = 'X'
        else:
            return 'Invalid player value'
        self.currentPlayer()
    
    def currentPlayer(self):
        self.text.set(f'The current player is: {self.value}')
        
class Game:
    def __init__(self, frame, sizeX = 3, sizeY = 3):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.frame = frame
        self.createBoard()
        self.text = StringVar()
        self.text.set('')
        self.gameOver = False
        
    def createBoard(self):
        self.board = []
        for row in range(self.sizeX):
            self.board.append([])
            
            for col in range(self.sizeY):
                id_no = row*3 + col
                self.board[row].append(Square(self.frame, row, col, id_no, game_font))
            print(self.board)
            
    def getBoard(self):
        self.currentBoard = []
        for row in range(self.sizeX):
            self.currentBoard.append([])
            for col in range(self.sizeY):
                self.currentBoard[row].append(self.board[row][col].squareText)
        self.currentBoard = np.array(self.currentBoard)
            
    def checkBoard(self):
        self.getBoard()
        for row in range(self.sizeX):
            arr = self.currentBoard[row,:]
            self.checkArr(arr)
        for col in range(self.sizeY):
            arr = self.currentBoard[:,col]
            self.checkArr(arr)
        arrD1 = self.currentBoard.diagonal()
        arrD2 = np.fliplr(self.currentBoard).diagonal()
        self.checkArr(arrD1)
        self.checkArr(arrD2)
        self.allClicked()
            
    def checkArr(self,arr):
        if len(np.unique(arr)) & (str(np.unique(arr)[0]) == 'X' or str(np.unique(arr)[0]) == '0'):
            print(f'You\'ve WON {player.value}')
            self.text.set(f'You\'ve WON {player.value}')
            win = Label(window, textvariable = self.text)
            win.pack()
            
            #refreshButton = Button(window, text = 'Play Again?', command = self.refresh())
            #refreshButton.pack()
            for row in range(self.sizeX):
                for col in range(self.sizeY):
                    self.board[row][col].change = False
    
    def allClicked(self):
        moves_left = 0
        for row in range(self.sizeX):
            for col in range(self.sizeY):
                moves_left += self.board[row][col].change
        print(moves_left)
        if moves_left == 1:
            self.text.set('The game is a Tie, try again?')
            win = Label(window, textvariable = self.text)
            win.pack()
            #refreshButton = Button(window, text = 'Play Again?', command = lambda: self.refresh())
            #refreshButton.pack()
            
    #def refresh(self):
    #    window.destroy()
    #    exec(open('./noughts_and_crosses.py').read()) 

player = Player()

game = Game(frame =input_frame)
window.mainloop()
