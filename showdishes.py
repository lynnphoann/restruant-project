from tkinter import *

class ShowDishes:
    def __init__(self,master):
        self.master = master
        self.setUpUi()

    def setUpUi(self):
        self.show_dishes_label = Label(self.master,text = 'Show Dishes').pack()