from tkinter import *

class UpadateDishes:
    def __init__(self,master):
        self.master = master
        self.setUpUi()

    def setUpUi(self):
        self.update_label = Label(self.master,text = "Update Dishes").pack()