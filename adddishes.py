from tkinter import *
import tkinter.messagebox

class AddDishes:
    def __init__(self,master,tools):
        self.tools = tools
        self.master = master
        self.setUpUi()

    def setUpUi(self):
        self.add_dishes_label = Label(self.master,text = "Add Dishes",relief = "solid",bg = "#1A1A19", fg = "#D1BB03",width = "20")
        self.add_dishes_label.grid(row = 0 ,columnspan =2 )

        self.name = Label(self.master,text = "Name")
        self.name.grid(row = 1,column = 0)

        self.name_e = Entry(self.master)
        self.name_e.grid(row = 1,column = 1)

        self.price = Label(self.master,text = "Price")
        self.price.grid(row = 2,column = 0)

        self.price_e = Entry(self.master)
        self.price_e.grid(row = 2, column = 1)


        self.btnClick = Button(self.master,text = "Confirm",command = self.insertdish)
        self.btnClick.grid(row = 3,column = 1,sticky = "e")

    def insertdish(self):
        nameGet =self.name_e.get()
        priceGet = self.price_e.get()

        # sql = """
        #     CREATE TABLE IF NOT EXISTS dishes(
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         name VARCHAR (100) NOT NULL,
        #         price INTEGER (6) NOT NULL
        #     )
        
        # """
        # self.tools.createTable(sql)
        self.tools.insertNewDish(nameGet,priceGet)
