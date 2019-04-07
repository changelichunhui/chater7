import os
def run(**args):
	print '[*] In dirlist'
	files=os.listdir('.')
	return str(files)