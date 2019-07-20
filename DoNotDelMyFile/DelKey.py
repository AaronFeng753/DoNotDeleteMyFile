#coding=utf-8
import fileinput
import re
import random
import os
import json
import sys
import os.path

def DelTheKey(filename,TheKey,filepath):
	f = open (filepath, "rb+")
	FileName=os.path.splitext(filename)[0]
	FileExt=os.path.splitext(filename)[1]
	current_dir = os.path.dirname(os.path.abspath(__file__))
	OriginalPath = current_dir + '\\Original\\'
	if os.path.exists(OriginalPath) == False:
		os.mkdir(OriginalPath)
	open(OriginalPath+FileName+FileExt, 'wb+').write(re.sub(bytes(TheKey,encoding = 'utf8'),bytes(),f.read()))
	f.close()
	print("\nSuccess!\n")
	
def ReadFileAndKey(filename):
	FileAndKey={}
	try:
		with open('FileAndKey.json','r') as f:
			FileAndKey=json.load(f)
	except FileNotFoundError:
		print('FileAndKey.json is missing!!')
	
	for key,value in FileAndKey.items():
		if key == filename:
			return str(value)

print('===================================')
print('=  DoNotDeleteMyFile              =')
print('=  2019.7.19                      =')
print('=                                 =')
print('=  Delete The Key & Fake Decrypt  =')
print('===================================')
print('tip:you can drag file into the window and file path and file name will be autofilled')

while True:
	filepath = ''
	try:
		filepath = str(sys.argv[1])
	except IndexError:
		filepath = input('file path&name: ')
		filepath=filepath.strip('"')
	filename = str(os.path.basename(filepath))
	TheKey = ReadFileAndKey(filename)
	DelTheKey(filename,TheKey,filepath)

	
