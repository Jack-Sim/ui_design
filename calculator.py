from tkinter import *

# Create the main window
window = Tk()


class Calculator:
    
    def __init__(self, window, title='Calculator'):
        self.window = window
        self.window.geometry('462x374')
        self.window.resizable(0,0)
        self.window.title('Calculator')
        self.expression = ''
        self.input_text = StringVar()
        
        self.build_calc()
    
    def build_calc(self):
        # Create an input window
        self.input_frame = Frame(self.window, width=312, height=50, bd=0, highlightbackground='black', highlightcolor='black', highlightthickness=1)
        self.input_frame.pack(side=TOP)
        
        # Put the input_text object into the input_frame
        self.input_field = Entry(self.input_frame, font=('arial', 18,'bold'), textvariable=self.input_text, width=50, bg = '#eee', bd=0, justify=RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        
        # Create frame for buttons
        self.btns_frame = Frame(self.window, width=312, height=272.5, bg='grey')
        self.btns_frame.pack()
        
        # First row of buttons
        self.clear = Button(self.btns_frame, text='C', fg = 'black', width=36, height=3, bd=0, bg='#eee', cursor='hand2', command = lambda: self.btn_clear())
        self.clear.grid(row=0,column=0,columnspan=3,padx=0,pady=0)
        self.divide = Button(self.btns_frame, text='/',fg = 'black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command = lambda: self.btn_click('/'))
        self.divide.grid(row=0,column=3, padx=1, pady=1)
        
        # Second row of buttons
        self.seven = Button(self.btns_frame, text='7',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(7))
        self.eight = Button(self.btns_frame, text='8',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(8))
        self.nine = Button(self.btns_frame, text='9',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(9))
        self.multiply = Button(self.btns_frame, text='*',fg = 'black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command = lambda: self.btn_click("*"))
        self.seven.grid(row=1, column=0, padx=1, pady=1)
        self.eight.grid(row=1, column=1, padx=1, pady=1)
        self.nine.grid(row=1, column=2, padx=1, pady=1)
        self.multiply.grid(row=1, column=3, padx=1, pady=1)
        
        
        # Second row of buttons
        self.four = Button(self.btns_frame, text='4',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(4))
        self.five = Button(self.btns_frame, text='5',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(5))
        self.six = Button(self.btns_frame, text='6',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(6))
        self.minus = Button(self.btns_frame, text='-',fg = 'black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command = lambda: self.btn_click("-"))
        self.four.grid(row=2, column=0, padx=1, pady=1)
        self.five.grid(row=2, column=1, padx=1, pady=1)
        self.six.grid(row=2, column=2, padx=1, pady=1)
        self.minus.grid(row=2, column=3, padx=1, pady=1)
        
        # Third row of buttons
        self.one = Button(self.btns_frame, text='1',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(1))
        self.two = Button(self.btns_frame, text='2',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(2))
        self.three = Button(self.btns_frame, text='3',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(3))
        self.plus = Button(self.btns_frame, text='+',fg = 'black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command = lambda: self.btn_click("+"))
        self.one.grid(row=3, column=0, padx=1, pady=1)
        self.two.grid(row=3, column=1, padx=1, pady=1)
        self.three.grid(row=3, column=2, padx=1, pady=1)
        self.plus.grid(row=3, column=3, padx=1, pady=1)
        
        # Last row of buttons
        self.zero = Button(self.btns_frame, text='0',fg = 'black', width=23, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click(0))
        self.point = Button(self.btns_frame, text='.',fg = 'black', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command = lambda: self.btn_click('.') )
        self.equals = Button(self.btns_frame, text='=',fg = 'black', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command = lambda: self.btn_equals())
        self.zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        self.point.grid(row=4, column=2, padx=1, pady=1)
        self.equals.grid(row=4, column=3, padx=1, pady=1)
        
    def btn_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)
        
    def btn_clear(self):
        self.expression = ''
        self.input_text.set(self.expression)
        
    def btn_equals(self):
        self.result = str(eval(self.expression))
        self.input_text.set(self.result)
        self.expression = ""
        
gui = Calculator(window)
window.mainloop()