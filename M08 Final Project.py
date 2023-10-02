__auther__ = "Kaden Stephens"
# 09/24/23
# This program

import datetime
import tkinter as tk
from tkinter import PhotoImage

# create main window
mainWin= tk.Tk()
mainWin.geometry("900x500")
mainWin.configure(bg="#00B7DF")
mainWin.title("KS Helpdesk Ticket System" )


    

#image = PhotoImage(file="M08/HomeButton.png") 

#HomeButton = tk.Button(mainWin, image=image, )
#HomeButton.pack()

# create instruction label
instructionLabel= tk.Label(mainWin, text="Welcome to KS Helpdesk Ticket System,\nPlease select whether you want to create a new Help Ticket or view an existing one.", bg="#00B7DF", fg="#000000", font="Helvetica 20")
instructionLabel.grid(column=0, row=0, padx=10, pady=10, columnspan=2) 

# create button to call second window




# start main window
mainWin.mainloop()