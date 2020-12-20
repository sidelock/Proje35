from tkinter import *
import sys
import os
from OLOG import *
from YLOG import *





def mainnscreen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x300")

    main_screen['background'] = '#FF0000'
    Label(text="Lütfen Seçim Yapınız.", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Yönetici Girişi 1", height="2", width="30", command=login1)
    Button.pack()
    Label(text="").pack()
    Button(text="Öğretmen Girişi", height="2", width="30", command=main2_account_screen)
    Button.pack()
    mainnscreen.mainloop()


mainnscreen()
