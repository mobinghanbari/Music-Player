import pygame
from pygame import mixer
from tkinter import *
import os

#Preparatory and elementary part of the program
root = Tk()
root.title('Music Player')

mixer.init()
songstatus = StringVar()
songstatus.set('Choosing')

#Playlist section
playlist = Listbox(root, selectmode=SINGLE)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\mobin\Music')
songs = os.listdir()

for song in songs:
    playlist.insert(END, song)


#The main functional part of the program
def playsong():
    current_song = playlist.get(ACTIVE)
    print(current_song)
    mixer.music.load(current_song)
    songstatus.set('Playing')
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