#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox 
class App(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='OK', command=self.hello)
        self.alterButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = App()
app.master.title('Hello')
app.mainloop()