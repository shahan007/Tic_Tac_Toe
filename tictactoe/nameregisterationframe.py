import tkinter as tk
from tkinter import ttk

class NameRegisterationFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__container = container
        self.__container.title('Tic Tac Toe Name Registeration')
        self.__container.resizable(False, False)
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure((0, 3), weight=1)
        self.create_widgets()
        self.place_widgets()

    @property
    def registerBtn(self):
        return self.__registerBtn

    def create_widgets(self):
        self.__title = ttk.Label(self, text='Player Name Registeration')
        self.__p1Holder = tk.StringVar(self, value='Player 1')
        self.__p1L = ttk.Label(self, text='Player 1 Name: ')
        self.__p1E = ttk.Entry(self, textvariable=self.__p1Holder)
        self.__p2Holder = tk.StringVar(self, value='Player 2')
        self.__p2L = ttk.Label(self, text='Player 2 Name: ')
        self.__p2E = ttk.Entry(self, textvariable=self.__p2Holder)
        self.__registerBtn = ttk.Button(self, text='Register', padding=10,
                                        command=lambda: self.register_players())

    def place_widgets(self):
        self.__title.grid(row=0, column=0, columnspan=2)
        self.__p1L.grid(row=1, column=0, sticky='E')
        self.__p1E.grid(row=1, column=1, sticky='W')
        self.__p2L.grid(row=2, column=0, sticky='E')
        self.__p2E.grid(row=2, column=1, sticky='W')
        self.__registerBtn.grid(
            row=3, column=0, columnspan=2, sticky='N', pady=25)

    def register_players(self):
        self.__container.style.theme_use(themename='solar')
        self.__container.title('Playing Tic Tac Toe')
        self.__container.resizable(True, True)
        game = self.__container.TicTacToeFrame
        game.nameMapping[1] = self.__p1Holder.get()
        game.nameMapping[2] = self.__p2Holder.get()
        game.update_status(
            text=f'Pending: Player {game.nameMapping[game.player] } Turn')
        game.tkraise()