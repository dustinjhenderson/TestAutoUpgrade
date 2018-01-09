#Dustin Henderson
#recover par files.
#/data/dustinhe/autoUpgrade/17.1/c10/
import os
from shutil import copyfile

def parsInput(text):
	text = text.strip(" ")
	text = text.lower()
	if text[0] == "y":
		return True
	else:
		return False

def getOperatingInput():
	targetDir = ""
	confirm = False
	print "What Directory?"
	targetDir = raw_input("dir: ")
	print "The Directory you entered is: ", targetDir, " is this correct?"
	confirm = raw_input("y/n:\n")
	confirm = parsInput(confirm)
	if(confirm == True):
		return targetDir
	else:
		exit()

'''
* pulled from the original script
'''
def findAllFilesOfType(fileExt): #pulled from original script
	"""
	Gets a list of all the files of a certain type in a directory
	:param file_ext: a string representing the file type to search for
	:return: a list of paths to all of the files with the given type and their
	"""
	# Make sure the file extension has a dot before it
	if fileExt[0] != ".":
		fileExt = "." + fileExt
	# Holds all of the files with the given extension
	fileList = []
	# Now recursively get all of the files with the given extension
	for dirpath, dirnames, filenames in os.walk("."):
		# Do not include the test directory when searching for files
		if "test" in dirnames:
			dirnames.remove("test")
		for filename in filenames:
			# If any of the files have the given extension, add it to the list of files found
			if filename.endswith(fileExt):
				# Get the full pathname of the qar file and add it to the list of files
				filepath = os.path.join(dirpath, filename)
				fileList.append(os.path.normpath(filepath))
	return fileList
	
'''----------------------------------------------------------------------------------------------------------------------------'''
'''******************************************************* MAIN ***************************************************************'''
'''----------------------------------------------------------------------------------------------------------------------------'''
targetDir = ""
parList = []

targetDir = getOperatingInput()
try:
	os.chdir(targetDir)
except:
	print "directory error"
	exit()

parList = findAllFilesOfType("par")

for fileName in parList:
	print copyfile(fileName, os.path.basename(fileName))
