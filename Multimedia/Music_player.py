from tkinter import *
import tkFileDialog as tk
import pygame

class Application(Frame, object):
	"""docstring for Application"""
	def __init__(self, master):
		super(Application, self).__init__(master)
		
		filemenu = Menu(root)
		filemenu.add_command(label = 'Open', command = self.openFile)
		root.config(menu = filemenu)

		self.flag = 0
		self.fileName = ""

		self.grid(rowspan = 5, columnspan = 4)
		self.titleLabel = Label(text = self.fileName)
		self.playButton = Button(text = 'Play', command = self.play_music)
		self.pauseButton = Button(text = 'Pause', command = self.pause_music)
		self.stopButton = Button(text = 'Stop', command = self.stop_music)

		self.titleLabel.grid(row = 0, column = 4, pady = 10)
		self.playButton.grid(row = 	3, column = 3, padx = 2, pady = 5)
		self.pauseButton.grid(row = 3, column = 4, padx = 2, pady = 5)
		self.stopButton.grid(row = 3, column = 5, padx = 2, pady = 5)

		pygame.init()

	def play_music(self):
		if self.flag == 1:
			pygame.mixer.music.unpause()

		else:
			if self.fileName != '':
				pygame.mixer.music.load(self.fileName)
				self.titleLabel['text'] = self.fileName
				pygame.mixer.music.play(0, 0.0)

	def pause_music(self):
		pygame.mixer.music.pause()
		self.flag = 1

	def stop_music(self):
		self.titleLabel['text'] = ""
		pygame.mixer.music.stop()

	def openFile(self):
		openFile = tk.askopenfile(mode = 'r')
		self.fileName = openFile.name
		self.titleLabel['text'] = self.fileName

root = Tk()
root.title('Music Player')
root.geometry('500x500')

app = Application(root)
app.mainloop()