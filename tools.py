from tkinter import *
import tkinter.messagebox
import sqlite3

class Tools:
    def __init__(self):
        self.conn = sqlite3.connect("restaurant.db")
        self.con = self.conn.cursor()


    def raiseFrame(self,frame):
        frame.tkraise()

    def createTable(self,sql):
        self.con.execute(sql)
        self.conn.commit()

    def insertNewDish(self,name,price):
        test = self.checkName(name)
        if test:
            tkinter.messagebox.showwarning("Warning!","Dish that name already exists")
        else :
            sql = """INSERT INTO dishes (name,price) VALUES (?,?)"""
            self.con.execute(sql,(name,price))
            self.conn.commit()
            tkinter.messagebox.showinfo("Success","Insert Complete!!")

    def checkName(self,name):
        sql = """SELECT * FROM dishes where name = ?"""
        result = self.con.execute(sql,[name])
        self.conn.commit()
        return len(result.fetchall())>0