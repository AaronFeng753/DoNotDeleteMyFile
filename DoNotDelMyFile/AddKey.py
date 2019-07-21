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
			FileAndKey=json.load(f)
	except FileNotFoundError:
		with open('FileAndKey.json','w+') as f:
			f.write('{}')
	FileAndKey[filename]=TheKey
	with open('FileAndKey.json','w+') as f:
		json.dump(FileAndKey,f,ensure_ascii=False)

		

print('=======================')
print('=  DoNotDeleteMyFile') 
print('=  2019.7.21') 
print('=') 
print('=  向文件末尾添加Key') 
print('=======================')
print('输入文件路径+名称(例:C:\\Users\\123\\Desktop\\images.jpg),然后按Enter')
print('tip:你可以直接把文件拖拽到窗口内,文件路径和名称会自动填写\n')

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
	
