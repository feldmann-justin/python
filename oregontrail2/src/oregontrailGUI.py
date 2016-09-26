'''
Created on Apr 21, 2016

@author: bf197158
'''
from pydoc import plaintext
from tkinter import *
from oregontrailgame import oregontrailgame

class OregonTrail(Frame):
    def __init__(self):
        '''Sets up the window and widgets.'''
        Frame.__init__(self)
        self.master.title("Oregon Trail")
        self.master.geometry('649x450')
        self.grid()
        
        canvas = Canvas(self, width = 649, height = 200)
        self._gif1 = PhotoImage(file = 'oregontrail.gif')
        self._imageLabel = Label(self, image = self._gif1)
        self._imageLabel.grid(row = 0, column = 0, columnspan = 3, sticky = N+W)
        
        self._textOutput = Text(self,
                               width = 80,
                               height = 10)
        self._textOutput.grid(row = 1, column = 0, columnspan = 3, sticky = W+E+N+S)
        #self._textOutput.config(state = 'disabled')
        self._textOutput.rowconfigure(0, weight = 2)
        self._textOutput.columnconfigure(0, weight = 2)
        #self._textOutput.insert(1.0, oregontrailgame.intro())
        
        self._choiceLabel = Label(self,
                                  text = "Make your choice below: ")
        self._choiceLabel.grid(row = 2, column = 1)
        
        '''Sets up the option buttons.'''
        self._oneBtn = Button(self, text = "1", command = self._one)
        self._oneBtn.config(font = ('helvetica', 15))
        self._oneBtn.grid(row = 3, column = 0)
        
        self._twoBtn = Button(self, text = "2", command = self._two)
        self._twoBtn.config(font = ('helvetica', 15))
        self._twoBtn.grid(row = 3, column = 1)
        
        self._threeBtn = Button(self, text = "3", command = self._three)
        self._threeBtn.config(font = ('helvetica', 15))
        self._threeBtn.grid(row = 3, column = 2)
        
        otg = oregontrailgame()
        self._write(otg.intro())
        
        
        
        
        
        
        
    def _one(self):
            x = 1
            #print("1")
            self._write(1)  
            
    def _two(self):
            x = 2
            #print("2")
            self._write(2)
    def _three(self):
            x = 3
            #print("3")
            self._write(3)
            
    def _write(self, txt):
        #self.output.insert()
        self._textOutput.insert(1.0, txt)
        
#