# Пример 1.27.PP4E/Preview/customizegui.py

from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):                           # наследует метод __init__
    def reply(self):                              # замещает метод reply
        showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()