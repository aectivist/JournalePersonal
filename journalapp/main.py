from customtkinter import *
from tkinter import *
from pymongo import MongoClient


window = CTk()

window.title("Journal")
window.geometry("900x600") #fml
window.minsize(900, 600)
window.maxsize(900,600)
set_appearance_mode("light")

cluster = MongoClient("mongodb+srv://Aectivistyrn:Y9eBpH2SGN2TR19Z@cluster0.pkkwg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["journaldata"]
data = db["data"]
logs = db["logs"]
userlogin = db["user"]

TabFrame_UpperPanel = CTkFrame(window, width = 900, height = 60, corner_radius=0, fg_color="#121212")
TabFrame_LeftPanel = CTkFrame(window, width =200, height=540, corner_radius=0, fg_color="#3052c9")
TabContentScroll = CTkScrollableFrame(window, width = 700, height = 540, corner_radius=0, fg_color="#bebdff")

TabFrame_UpperPanel.place(x=0, y=0)
TabFrame_LeftPanel.place(x=0, y = 60)
TabContentScroll.place(x=200, y=60)

TabFrame_LeftPanel.grid_propagate(0)

TitleFontUpperPanel = CTkFont(size=20, weight="bold")
PersonalJournalLabel = CTkLabel(TabFrame_UpperPanel, text="Aect's Personal Journal", text_color="#FFFFFF", font=TitleFontUpperPanel)
PersonalJournalLabel.place(x=10, y=15)

#BUTTONS----

ButtonFontLeftPannel = CTkFont(size=15, weight="bold")
button_NewNote = CTkButton(TabFrame_LeftPanel, width=170, height=55, text="Home", corner_radius=0, fg_color="#0b248f", font=ButtonFontLeftPannel, border_width=2, border_color="#7d92f0",hover_color="#223db3")
button_NewNote.grid(row=0,column=0,pady=10)


button_NewNote = CTkButton(TabFrame_LeftPanel, width=170, height=55, text="New Note", corner_radius=0, fg_color="#0b248f", font=ButtonFontLeftPannel, border_width=2, border_color="#7d92f0",hover_color="#223db3")
button_NewNote.grid(row=1,column=0,pady=5)


button_archive = CTkButton(TabFrame_LeftPanel, width=170, height=55, text="Archive", corner_radius=0, fg_color="#0b248f", font=ButtonFontLeftPannel, border_width=2, border_color="#7d92f0",hover_color="#223db3")
button_archive.grid(row=2,column=0,pady=10)


button_login = CTkButton(TabFrame_LeftPanel, width=170, height=90, text="Login", corner_radius=0, fg_color="#000000", font=ButtonFontLeftPannel, border_width=2, border_color="#000000", hover_color="#1a1a1a")
button_login.place(x=15, y=430)


for i in range(1):
            TabFrame_LeftPanel.grid_columnconfigure(i, weight=1, uniform="column")
            TabFrame_LeftPanel.grid_rowconfigure(0, minsize=51)

window.mainloop()
