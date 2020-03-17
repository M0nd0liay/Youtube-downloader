# script copy from: https://youtu.be/TnpXS7TdJlE
# Fix error from:  https://github.com/nficano/pytube/issues/473 & http://www.cdotson.com/2017/01/sslerror-with-python-3-6-x-on-macos-sierra/
# Pim Sweers 17/3/2020

import tkinter as tk
import os, time, re
from pytube import YouTube #pip3 install pytube3
from tkinter import *
from tkinter import messagebox, filedialog

# The body
def CreateWidgets(): 
	link = Label(scherm, text='YouTube link :', bg='#1f294e', fg='white')
	link.grid(row=1, column=0, padx=5, pady=5)

	scherm.linkText = Entry(scherm, width=55, textvariable=videolink)
	scherm.linkText.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

	opslaglabel = Label(scherm, text='Opslag locatie :', bg='#1f294e', fg='white')
	opslaglabel.grid(row=2, column=0, padx=5, pady=5)

	scherm.opslaglabelText = Entry(scherm, width=38, textvariable=downloadPath)
	scherm.opslaglabelText.grid(row=2, column=1, padx=5, pady=5)

	browse = Button(scherm, text='Browse', command=B_Browse, width=15)
	browse.grid(row=2, column=2, padx=5, pady=5 )

	dwld = Button(scherm, text='Download', command=A_Download, width=15)
	dwld.grid(row=3, column=1, padx=5, pady=5 )

#Download filepath
def B_Browse():
	dowloadDirectory = filedialog.askdirectory(initialdir='Directory here')
	downloadPath.set(dowloadDirectory)

# pytube use
def A_Download():
	yt_link = videolink.get()
	dwldFolder = downloadPath.get()
	getVideo = YouTube(yt_link)
	videoStream = getVideo.streams.filter(only_audio=True).first()
	videoStream.download(dwldFolder)

	#filepath for rename .mp4 to .mp3
	for root, dirs, files in os.walk(dwldFolder):
	    for filename in files:
	        basename, extension = os.path.splitext(filename)
	        if extension == '.mp4':
	            mp4_file = root + '/' + basename + extension
	            mp3_file = root + '/' + basename + '.mp3'

	os.rename(mp4_file, mp3_file)

	#Time for the rename file
	time.sleep(3)
	
	#massage efter is done
	messagebox.showinfo('Succesvol', 'MP3 is gedownload Groetjes Pim ;)" ')


scherm = Tk()
scherm.title('YouTube Downloader')
scherm.geometry('650x120')
scherm.resizable(False, False)
scherm.configure(background='#1f294e')

videolink = StringVar()
downloadPath = StringVar()

CreateWidgets()

scherm.mainloop()