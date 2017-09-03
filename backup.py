# BackupPythonpro
#The basic code to create and update backup from one directory to another.


import os, shutil
from shutil import copyfile

srce=raw_input("Enter source Path")
dest=raw_input("Enter Destination Path")
def backup(source,destination):
	pathsource, directories, files = os.walk(source).next()
	directories = sorted(directories)
	for f in files:
		src = source+'/'+f
		dst = destination+'/'+f
		copyfile(src,dst)
	if len(directories) > 0 :
		for f in directories:
			if os.path.exists(destination+'/'+f):
				print f+' exist'
			else:
				os.makedirs(destination+'/'+f)
				 
		for f in directories:
			src = source+'/'+f
			print src
			dst = destination+'/'+f
			print dst
			backup(src,dst)
		
		
backup(srce,dest)
