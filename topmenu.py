from tkinter import *

class TopMenu:
    def __init__(self,master,tools,frames):
        self.master = master
        self.frames = frames
        self.tools = tools
        self.setUpUi()

    def setUpUi(self):
        self.menu_bar = Menu(self.master)
        self.master.config(menu = self.menu_bar)

        self.dish_menu = Menu(self.menu_bar)

        self.dish_menu.add_command(label ="Show Dishes",command = lambda :self.tools.raiseFrame(self.frames["show_dishes"]))
        self.dish_menu.add_command(label ="add_dishes",command = lambda :self.tools.raiseFrame(self.frames["add_dishes"]))
        self.dish_menu.add_command(label ="update_dishes",command = lambda :self.tools.raiseFrame(self.frames["update_dishes"]))

        self.menu_bar.add_cascade(label = "Selection",menu = self.dish_menu)

