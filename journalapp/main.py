from customtkinter import *
from tkinter import *
from pymongo import MongoClient


window = CTk()

window.title("Journal")
window.geometry("900x600") #fml
window.minsize(0, 0)
set_appearance_mode("light")

cluster = MongoClient("mongodb+srv://Aectivistyrn:Y9eBpH2SGN2TR19Z@cluster0.pkkwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["journaldata"]
data = db["data"]
logs = db["logs"]
data = db["user"]

TabFrame_UpperPanel = CTkFrame(window, width = 900, height = 60, corner_radius=0)
TabFrame_Panel = CTkFrame(window, width =200, height=540, corner_radius=0)
TabFrame_UpperPanel.place(x=0, y=0)
TabFrame_Panel.place(x=0, y = 60)






window.mainloop()
