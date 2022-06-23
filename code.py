import pygame
from pygame import mixer
from tkinter import *
import os


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