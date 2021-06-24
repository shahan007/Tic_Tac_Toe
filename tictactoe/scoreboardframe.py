import tkinter as tk
from tkinter import ttk

class ScoreBoardFrame(ttk.Frame):

    # add database
    def __init__(self, container):
        super().__init__(container)
        self.__container = container
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 3, 5, 6), weight=1)
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.__title = ttk.Label(self, text='Score Card')
        self.__p1Score = ttk.Label(self)
        self.__p2Score = ttk.Label(self)
        self.update_score_display()
        self.__goBackBtn = ttk.Button(self, text='<-Go Back', padding=10,
                                      command=lambda: self.go_back_to_play())

    def place_widgets(self):
        self.__title.grid(row=0, column=0)
        ttk.Separator(self).grid(row=1, column=0, sticky='EW')
        self.__p1Score.grid(row=2, column=0)
        ttk.Separator(self).grid(row=3, column=0, sticky='EW')
        self.__p2Score.grid(row=4, column=0)
        ttk.Separator(self).grid(row=5, column=0, sticky='EW')
        self.__goBackBtn.grid(row=6, column=0)

    def update_score_display(self):
        game = self.__container.TicTacToeFrame
        self.__p1Score.config(
            text=f"Player {game.nameMapping[1]} Score is {game.scoreMapping[1]}")
        self.__p2Score.config(
            text=f"Player {game.nameMapping[2]} Score is {game.scoreMapping[2]}")

    def go_back_to_play(self):
        self.__container.style.theme_use(themename='solar')
        self.__container.title('Playing Tic Tac Toe')
        self.__container.resizable(True, True)
        self.__container.TicTacToeFrame.tkraise()