from tkinter import *
from topmenu import *
from showdishes import *
from updatedishes import *
from adddishes import *
from tools import *

class App(Tools):
    def __init__(self,master):
        self.master = master
        self.frames = {}
        self.tools = Tools()
        self.setUpUi()
        

    def setUpUi(self):
        self.frames["show_dishes"] = Frame(self.master)
        self.frames["add_dishes"]  = Frame(self.master)
        self.frames["update_dishes"] = Frame(self.master)

        TopMenu(self.master,self.tools,self.frames)

        ShowDishes(self.frames["show_dishes"])
        UpadateDishes (self.frames["update_dishes"])
        AddDishes(self.frames["add_dishes"],self.tools)


        for frame in self.frames.values():
            frame.grid(row= 0,column = 0,sticky = "news")
        
        self.tools.raiseFrame(self.frames["show_dishes"])




root = Tk()
App(root)
root.title("Dish Application")
root.mainloop()