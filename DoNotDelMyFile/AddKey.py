import fileinput
import re
import random
import os
import json
import sys
import os.path

def AddTheKey(filename,TheKey):
		with open(filename,'a') as f:
			f.write(TheKey)
		print("\nSuccess!\n")
		
def GenerateTheKey():
	randomint = str(random.randint(10000,9999999))
	randomdata = randomint
	return '#DoNotDelMyFile//'+ randomdata +'#'

def SaveFileAndKey(filename,TheKey):
	FileAndKey={}
	try:
		with open('FileAndKey.json','r') as f:
			FileAndKey=json.load(f)
	except FileNotFoundError:
		with open('FileAndKey.json','w+') as f:
			f.write('{}')
	FileAndKey[filename]=TheKey
	with open('FileAndKey.json','w+') as f:
		json.dump(FileAndKey,f)

		

print('=======================')
print('=  DoNotDeleteMyFile  =')
print('=  2019.7.19          =')
print('=                     =')
print('=  Add The Key        =')
print('=======================')

while True:
	filename = ''
	try:
		filename = str(sys.argv[1])
	except IndexError:
		filename = input('file name: ')
	TheKey = GenerateTheKey()
	AddTheKey(filename,TheKey)
	filename = str(os.path.basename(filename))
	SaveFileAndKey(filename,TheKey)
	
