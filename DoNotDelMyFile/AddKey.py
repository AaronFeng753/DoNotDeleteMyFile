#coding=utf-8
import fileinput
import re
import random
import os
import json
import sys
import os.path


def AddTheKey(filename,TheKeym,filepath):
	f = open (filepath, "rb+")
	FileName=os.path.splitext(filename)[0]
	FileExt=os.path.splitext(filename)[1]
	current_dir = os.path.dirname(os.path.abspath(__file__))
	KeyAddedPath = current_dir + '\\KeyAdded\\'
	if os.path.exists(KeyAddedPath) == False:
			os.mkdir(KeyAddedPath)
	open(KeyAddedPath+FileName+FileExt, 'wb+').write(f.read())
	open(KeyAddedPath+FileName+FileExt, 'a+').write(TheKey)
	f.close()
	print("\nSuccess!\n")
		
def GenerateTheKey():
	randomint = str(random.randint(10000,9999999))
	randomdata = randomint
	return '#DoNotDelMyFile//'+ randomdata +'#'

def SaveFileAndKey(filename,TheKey):
	FileAndKey={}
	try:
		with open('FileAndKey.json','r') as f:
			FileAndKey=json.load(f,ensure_ascii=False)
	except FileNotFoundError:
		with open('FileAndKey.json','w+') as f:
			f.write('{}')
	FileAndKey[filename]=TheKey
	with open('FileAndKey.json','w+') as f:
		json.dump(FileAndKey,f,ensure_ascii=False)

		

print('=======================')
print('=  DoNotDeleteMyFile  =')
print('=  2019.7.19          =')
print('=                     =')
print('=  Add The Key        =')
print('=======================')
print('tip:you can drag file into the window and file path and file name will be autofilled')

while True:
	filepath = ''
	try:
		filepath = str(sys.argv[1])
	except IndexError:
		filepath = input('file path&name: ')
		filepath=filepath.strip('"')
	TheKey = GenerateTheKey()
	filename = str(os.path.basename(filepath))
	AddTheKey(filename,TheKey,filepath)
	SaveFileAndKey(filename,TheKey)
	
