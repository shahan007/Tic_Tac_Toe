import tkinter as tk
from tkinter import ttk

class TicTacToeFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.__container = container
        self.columnconfigure((0, 1, 2), weight=1)
        self.rowconfigure((0, 1, 5), weight=0)
        self.rowconfigure((2, 3, 4), weight=1)
        self.__player = 1
        self.__nameMapping = {1: 'Player 1', 2: 'Player 2'}
        self.__mapping = {1: 'X', 2: 'O'}
        self.__scoreMapping = {1: 0, 2: 0}
        self.__data = [[None, None, None] for i in range(3)]
        self.create_widgets()
        self.place_widgets()

    @property
    def ButtonPanelFrame(self):
        return self.__ButtonPanelFrame

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, newPlayer):
        self.__player = newPlayer

    @property
    def nameMapping(self):
        return self.__nameMapping

    @property
    def scoreMapping(self):
        return self.__scoreMapping

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, newData):
        self.__data = newData

    @property
    def play_tiles(self):
        return self.__buttons

    def create_widgets(self):
        self.__title = ttk.Label(self, text='Play Tic Tac Toe!')
        self.__status = ttk.Label(self)
        self.__buttons = []
        for i in range(9):
            button = ttk.Button(
                self, text='   ', style='success.Outline.TButton')  # new config
            button.config(
                command=lambda button=button: self.place_marker(button))
            self.__buttons.append(button)
        self.__ButtonPanelFrame = ButtonPanelFrame(self, self.__container)

    def place_widgets(self):
        self.__title.grid(row=0, column=0, columnspan=3, pady=10)
        self.__status.grid(row=1, column=0, columnspan=3, pady=10)
        index = 0
        for row in range(2, 5):
            for column in range(3):
                if column == 0:
                    xpadding = (50, 0)
                elif column == 2:
                    xpadding = (0, 50)
                else:
                    xpadding = (0, 0)
                self.__buttons[index].grid(
                    row=row, column=column, sticky='EWNS', padx=xpadding, pady=0)
                index += 1
        self.__ButtonPanelFrame.grid(
            row=row+1, column=0, columnspan=3, sticky='EW')

    def place_marker(self, button):
        marker = self.__mapping.get(self.__player)
        grid_info = button.grid_info()
        row, column = grid_info.get('row'), grid_info.get('column')
        self.__data[row-2][column] = self.__player
        button.config(text=f'{marker}', state=tk.DISABLED)
        self.__ButtonPanelFrame.updateNameBtn.config(state=tk.DISABLED)
        if self.check_win():
            self.update_status(
                text=f'Winner: Player {self.__nameMapping[self.__player]} Won !!! ')
            self.__scoreMapping[self.__player] += 1
            # switch off everything here disable all
            self.state_playBtns(state=tk.DISABLED)
            self.__ButtonPanelFrame.playAgainBtn.config(state=tk.NORMAL)
            self.__ButtonPanelFrame.updateNameBtn.config(state=tk.NORMAL)
        else:
            if self.check_game_over():
                self.update_status(text=f'DRAW: Good Luck playing next time!')
                self.__ButtonPanelFrame.playAgainBtn.config(state=tk.NORMAL)
                self.__ButtonPanelFrame.updateNameBtn.config(state=tk.NORMAL)
            else:
                self.switch_players()

    def check_win(self):
        #check horizontal
        for row in range(3):
            if self.__data[row][0] != self.__player:
                continue
            status = all(
                [value == self.__player for value in self.__data[row][1:]])
            if status:
                return True

        #check veritcal
        for column in range(3):
            if self.__data[0][column] != self.__player:
                continue
            status = all([self.__data[value][column] ==
                          self.__player for value in range(1, 3)])
            if status:
                return True

        #check diagnol
        middle = self.__data[1][1]
        if middle != self.__player:
            return False

        for index in range(0, 2):
            firstRow = self.__data[0][2 * index]
            lastRow = self.__data[-1][index-1]
            if firstRow == self.__player and lastRow == self.__player:
                return True
        return False

    def check_game_over(self):
        for t in range(len(self.__data)):
            if self.__data[0][t] == None or self.__data[1][t] == None or self.__data[2][t] == None:
                return False
        return True

    def switch_players(self):
        if self.__player == 1:
            self.__player = 2
        else:
            self.__player = 1
        self.update_status(
            text=f'Pending: Player {self.__nameMapping[self.__player]} Turn')

    def update_status(self, text):
        self.__status.config(text=text)

    def state_playBtns(self, state):
        for btn in self.__buttons:
            btn.config(state=state)


class ButtonPanelFrame(ttk.Frame):

    def __init__(self, container, rootwindow):
        super().__init__(container)
        self.__container = container
        self.__rootwindow = rootwindow
        self.columnconfigure((0, 1, 2), weight=1)
        self.create_widgets()
        self.place_widgets()

    @property
    def updateNameBtn(self):
        return self.__updateNameBtn

    @property
    def checkScrBtn(self):
        return self.__checkScrBtn

    @property
    def playAgainBtn(self):
        return self.__playAgainBtn

    def create_widgets(self):
        self.__updateNameBtn = ttk.Button(
            self, text='Update Name', padding=2, command=lambda: self.update_name(), width=12)
        self.__playAgainBtn = ttk.Button(
            self, text='Play Again', state=tk.DISABLED, padding=2, command=lambda: self.play_again(),
            width=12)
        self.__checkScrBtn = ttk.Button(
            self, text='Check Score', padding=2, command=lambda: self.check_scores(), width=12)

    def place_widgets(self):
        self.__updateNameBtn.grid(
            row=0, column=0, columnspan=1, pady=8, sticky='E')
        self.__playAgainBtn.grid(row=0, column=1, columnspan=1, pady=8)
        self.__checkScrBtn.grid(row=0, column=2,
                                columnspan=1, pady=8, sticky='W')

    def update_name(self):
        self.__rootwindow.style.theme_use(themename='yeti')
        self.__rootwindow.NameRegisterationFrame.registerBtn.config(
            text='Update Names')
        self.play_again()
        self.__rootwindow.resizable(False, False)
        self.__rootwindow.NameRegisterationFrame.tkraise()

    def play_again(self):
        self.__playAgainBtn.config(state=tk.DISABLED)
        self.__container.data = [[None, None, None] for i in range(3)]
        self.__container.player = 1
        self.__container.state_playBtns(state=tk.NORMAL)
        self.__container.update_status(
            text=f'Pending: Player {self.__container.nameMapping[self.__container.player]} Turn')
        for btn in self.__container.play_tiles:
            btn.config(text='   ')

    def check_scores(self):
        self.__rootwindow.style.theme_use(themename='yeti')
        self.__rootwindow.ScoreBoardFrame.update_score_display()
        self.__rootwindow.title('Score Card')
        self.__rootwindow.resizable(False, False)
        self.__rootwindow.ScoreBoardFrame.tkraise()