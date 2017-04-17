# Questions 6

import json
from Tkinter import *
import ttk

class App:

    value_of_combo = 'X'

    def __init__(self, parent):
        self.parent = parent        	

    def combo(self):
    	with open('ca.json') as data_file:    
    		data = json.load(data_file)
		citiesList = [x['name'] for x in data]
		citiesList.sort()
    	self.box_value = StringVar()
    	self.box = ttk.Combobox(self.parent, textvariable=self.box_value)
    	self.box['values'] = citiesList
    	self.box.current(0)
    	self.box.bind("<<ComboboxSelected>>", selectedMethod(self))
    	self.box.grid(column=0, row=0)

def selectedMethod(self):
	print("method is called")
	print(self.box.get())

if __name__ == '__main__':
    root = Tk()
    app = App(root)
    app.combo()
    root.mainloop()
	