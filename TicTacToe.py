import tkinter as tk
import tkinter.ttk as ttk

def main():

    root = tk.Tk()
    GameUI(root)
    root.mainloop()


class GameUI(ttk.Frame):

    game = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
        ]
    gameCount = 0
    XWin = 0
    OWin = 0

    def __init__(self, master):
        super().__init__(master)
        self.master  = master
        self.master_configure()


        self.place(relx=.05, rely=.05, relheight=.85, relwidth=.90)
        self.style = ttk.Style()
        self.style.configure('TFrame', background='white')
        self.style.configure('TLabel', background='black', foreground='white', font=('verdana',14,'bold'))

        self.XText = ttk.Label(self.master, text='X - ' + str(self.XWin))
        self.OText = ttk.Label(self.master, text='O - ' + str(self.OWin))
        self.XText.place(relx=.05)
        self.OText.place(relx=.86)

        self.Retry = ttk.Button(self.master, text='Retry', style='Retry.TButton', command=self.wipe)
        self.Retry.place(relx=.40, rely=.92, relwidth=.2)

        self.buttons()

    def master_configure(self):

        self.master.title('TicTacToe')
        self.master.geometry('600x600')
        self.master.configure(bg='black')

    def buttons(self):

        self.style.configure('TButton', borderwidth=2, relief='solid', font=('Verdana', 100, 'bold'),
                             foreground='blue')
        self.style.configure('X.TButton', borderwidth=2, relief='solid', font=('Verdana', 100, 'bold'),
                             foreground='red')
        self.style.configure('Retry.TButton', borderwidth=2, relief='solid', font=('Verdana', 16, 'bold'),
                             foreground='black')
        self.style.map('TButton', foreground=[('disabled', 'blue')])
        self.style.map('X.TButton', foreground=[('disabled', 'red')])

        self.button1 = ttk.Button(self, text=self.game[0][0], command= lambda: self.click(self.button1,0,0))
        self.button1.grid(row=0, column=0, sticky='nsew')
        self.button2 = ttk.Button(self, text=self.game[0][1], command= lambda: self.click(self.button2,0,1))
        self.button2.grid(row=0, column=1, sticky='nsew')
        self.button3 = ttk.Button(self, text=self.game[0][2], command= lambda: self.click(self.button3,0,2))
        self.button3.grid(row=0, column=2, sticky='nsew')

        self.button4 = ttk.Button(self, text=self.game[1][0], command= lambda: self.click(self.button4,1,0))
        self.button4.grid(row=1, column=0, sticky='nsew')
        self.button5 = ttk.Button(self, text=self.game[1][1], command= lambda: self.click(self.button5,1,1))
        self.button5.grid(row=1, column=1, sticky='nsew')
        self.button6 = ttk.Button(self, text=self.game[1][2], command= lambda: self.click(self.button6,1,2))
        self.button6.grid(row=1, column=2, sticky='nsew')

        self.button7 = ttk.Button(self, text=self.game[2][0], command= lambda: self.click(self.button7,2,0))
        self.button7.grid(row=2, column=0, sticky='nsew')
        self.button8 = ttk.Button(self, text=self.game[2][1], command= lambda: self.click(self.button8,2,1))
        self.button8.grid(row=2, column=1, sticky='nsew')
        self.button9 = ttk.Button(self, text=self.game[2][2], command= lambda: self.click(self.button9,2,2))
        self.button9.grid(row=2, column=2, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def click(self, button, num1, num2):

        self.gameCount += 1

        if self.gameCount % 2 == 0:
            button['state'] = 'disabled'
            button['text'] = 'X'
            button['style'] = 'X.TButton'
            self.game[num1][num2] = 'X'
            self.win()

        else:
            button['state'] = 'disabled'
            button['text'] = 'O'
            button['style'] = 'TButton'
            self.game[num1][num2] = 'O'
            self.win()

    def win(self):

        if self.game[0][0] == 'X' and self.game[0][1] == 'X' and self.game[0][2] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[1][0] == 'X' and self.game[1][1] == 'X' and self.game[1][2] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[2][0] == 'X' and self.game[2][1] == 'X' and self.game[2][2] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[0][0] == 'X' and self.game[1][0] == 'X' and self.game[2][0] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[0][1] == 'X' and self.game[1][1] == 'X' and self.game[2][1] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[0][2] == 'X' and self.game[1][2] == 'X' and self.game[2][2] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[0][0] == 'X' and self.game[1][1] == 'X' and self.game[2][2] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[2][0] == 'X' and self.game[1][1] == 'X' and self.game[0][2] == 'X':
            print('X Win.')
            self.XWin += 1
            self.XText['text'] = 'X - ' + str(self.XWin)
            self.disabledall()

        elif self.game[0][0] == 'O' and self.game[0][1] == 'O' and self.game[0][2] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

        elif self.game[1][0] == 'O' and self.game[1][1] == 'O' and self.game[1][2] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

        elif self.game[2][0] == 'O' and self.game[2][1] == 'O' and self.game[2][2] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

        elif self.game[0][0] == 'O' and self.game[1][0] == 'O' and self.game[2][0] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

        elif self.game[0][1] == 'O' and self.game[1][1] == 'O' and self.game[2][1] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

        elif self.game[0][2] == 'O' and self.game[1][2] == 'O' and self.game[2][2] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

        elif self.game[0][0] == 'O' and self.game[1][1] == 'O' and self.game[2][2] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

        elif self.game[2][0] == 'O' and self.game[1][1] == 'O' and self.game[0][2] == 'O':
            print('O Win.')
            self.OWin += 1
            self.OText['text'] = 'O - ' + str(self.OWin)
            self.disabledall()

    def disabledall(self):

        self.button1['state'] = 'disabled'
        self.button2['state'] = 'disabled'
        self.button3['state'] = 'disabled'
        self.button4['state'] = 'disabled'
        self.button5['state'] = 'disabled'
        self.button6['state'] = 'disabled'
        self.button7['state'] = 'disabled'
        self.button8['state'] = 'disabled'
        self.button9['state'] = 'disabled'

    def wipe(self):

        self.game = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
            ]

        self.button1['text'] = ' '
        self.button2['text'] = ' '
        self.button3['text'] = ' '
        self.button4['text'] = ' '
        self.button5['text'] = ' '
        self.button6['text'] = ' '
        self.button7['text'] = ' '
        self.button8['text'] = ' '
        self.button9['text'] = ' '

        self.button1['state'] = 'active'
        self.button2['state'] = 'active'
        self.button3['state'] = 'active'
        self.button4['state'] = 'active'
        self.button5['state'] = 'active'
        self.button6['state'] = 'active'
        self.button7['state'] = 'active'
        self.button8['state'] = 'active'
        self.button9['state'] = 'active'


if __name__ == '__main__':
    main()



