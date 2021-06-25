import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from .nameregisterationframe import NameRegisterationFrame
from .tictactoeframe import TicTacToeFrame
from .scoreboardframe import ScoreBoardFrame

class RootWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.set_dpi_awareness()
        self.__style = Style(theme='yeti')  # new
        self.__style.master = self
        self.geometry('300x300')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.__NameRegisterationFrame = NameRegisterationFrame(self)
        self.__TicTacToeFrame = TicTacToeFrame(self)
        self.__ScoreBoardFrame = ScoreBoardFrame(self)
        self.__NameRegisterationFrame.grid(row=0, column=0, sticky='NESW')
        self.__TicTacToeFrame.grid(row=0, column=0, sticky='NESW')
        self.__ScoreBoardFrame.grid(row=0, column=0, sticky='NESW')
        self.__NameRegisterationFrame.tkraise()

    @property
    def NameRegisterationFrame(self):
        return self.__NameRegisterationFrame

    @property
    def TicTacToeFrame(self):
        return self.__TicTacToeFrame

    @property
    def ScoreBoardFrame(self):
        return self.__ScoreBoardFrame

    @property
    def style(self):
        return self.__style

    def set_dpi_awareness(self, level=1):
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(level)
        except:
            pass