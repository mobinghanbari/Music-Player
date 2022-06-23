import pygame
from pygame import mixer
from tkinter import *
import os

#Preparatory and elementary part of the program
root = Tk()
root.title('Music Player')
root.resizable(False, False)

mixer.init()
songstatus = StringVar()
songstatus.set('Choosing')

#Playlist section
playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

get_username = os.getlogin()
os.chdir(r'C:\Users\{}\Music'.format(get_username))
songs = os.listdir()

for song in songs:
    playlist.insert(END, song)


#The main functional part of the program
def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set('Paused')
    mixer.music.pause()

def stopsong():
    songstatus.set('Stopped')
    mixer.music.stop()

def resumesong():
    songstatus.set('Resuming')
    mixer.music.unpause()

#Button section
playbtn = Button(root, text='Play', command=playsong)
playbtn.config(font=('arial', 20), bg='DodgerBlue2', fg='black', padx=7, pady=7)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text='Pause', command=pausesong)
pausebtn.config(font=('arial', 20), bg='DodgerBlue2', fg='black', padx=7, pady=7)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text='Stop', command=stopsong)
stopbtn.config(font=('arial', 20), bg='DodgerBlue2', fg='black', padx=7, pady=7)
stopbtn.grid(row=1, column=2)

resumebtn = Button(root, text='Resume', command=resumesong)
resumebtn.config(font=('arial', 20), bg='DodgerBlue2', fg='black', padx=7, pady=7)
resumebtn.grid(row=1, column=3)

root.mainloop()