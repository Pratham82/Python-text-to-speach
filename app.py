import os
import pyttsx3
import PyPDF2
import keyboard

def simpleSpeaker():
	entries = os.listdir('Files/')
	print('These are the available file in your current folder: ')
	print(*(f for f  in entries), sep='\n')
	fName = input('Choose the file to read:\n')

	#* Get the path of Files folder
	folderDir = os.path.join(os.getcwd(), 'Files')
	fileDir = os.path.join(folderDir, fName)


	#* For text files
	dataToRead = open(fileDir, 'r')
	mySpeaker = pyttsx3.init()
	mySpeaker.say(f'Now reading {fName}')
	
	for l in dataToRead:
		mySpeaker.say(l)
		mySpeaker.runAndWait()

	return 

simpleSpeaker()