import fileinput
import re
import random
import os
import json
import sys
import os.path

def DelTheKey(filename,TheKey):
	f = open (filename, "rb+")
	FileName=os.path.splitext(filename)[0]
	FileExt=os.path.splitext(filename)[1]
	open(FileName+'_Original'+FileExt, 'wb+').write(re.sub(bytes(TheKey,encoding = 'utf8'),bytes(),f.read()))
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

print('=======================')
print('=  DoNotDeleteMyFile  =')
print('=  2019.7.19          =')
print('=                     =')
print('=  Delete The Key     =')
print('=======================')

while True:
	filename = ''
	try:
		filename = str(sys.argv[1])
	except IndexError:
		filename = input('file name: ')
	filename = str(os.path.basename(filename))
	TheKey = ReadFileAndKey(filename)
	DelTheKey(filename,TheKey)
	
