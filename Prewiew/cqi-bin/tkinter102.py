# Пример 1.25.PP4E\Preview\tkinter102.py

"""
В примере 1.25 приводится переработанная
версия предыдущего сценария с одной кнопкой, в которой графический
интерфейс реализован в виде класса.
"""

from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='Button pressed')

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
