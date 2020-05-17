from requests import post
from tkinter import *
from tkinter import messagebox
import sys
import requests
import json
import os

class Gui():
    def main(self):
        self.root = Tk()
        self.fileName = r"config.json"
        if os.path.exists(self.fileName) == True:
            self.json_read = open('config.json', 'r')
            self.json_value = json.load(self.json_read)
            self.json_token = self.json_value['Token']
            self.bye()
        else:
            label = Label(self.root, text='Bot token')
            confirmBtn = Button(self.root, text='Login', command=lambda: self.validate())
            self.tokenE = Entry(self.root, width=50)
            self.tokenE.pack()
            label.pack()
            confirmBtn.pack()
            self.root.mainloop()

    def validate(self):
        self.token = self.tokenE.get()
        self.user = ({"Token": self.token})
        with open('config.json', 'a') as file:
            json.dump(self.user, file, indent=4)
        self.json_read = open('config.json', 'r')
        self.json_value = json.load(self.json_read)
        self.json_token = self.json_value['Token']
        self.bye()
    def bye(self):
        self.root.destroy()

