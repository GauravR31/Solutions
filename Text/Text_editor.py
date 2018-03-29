import sys
from Tkinter import *
import tkFileDialog as tk
import tkMessageBox as tk2

v=sys.version

class Editor(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.master = master
		self.create()

	def create(self):
		self.text1 = Text(width=20, height=20)
		self.text1.pack(expand=YES, fill=BOTH)

		filemenu = Menu(root)
		filemenu.add_command(label = 'New', command = self.newDoc)
		filemenu.add_command(label = 'Save', command = self.saveAs)
		filemenu.add_command(label = 'Open', command = self.openDoc)
		root.config(menu=filemenu)

	def newDoc(self):
		if tk2.askyesno("Message", "Unsaved work will be lost. Continue?"):
			self.text1.delete(1.0, END)

	def saveAs(self):
		t = str(self.text1.get("1.0", "end-1c"))
		saveLocation = tk.asksaveasfilename(defaultextension=".txt")
		file1 = open(saveLocation, "w+")
		file1.write(t)
		file1.close()

	def openDoc(self):
		openFile = tk.askopenfile(mode = 'r')
		text = openFile.read()
		self.text1.insert(END, text)
		openFile.close()

root= Tk()
root.title('Text Editor')
root.geometry('700x600')

editor = Editor(root)
editor.mainloop()