#Dustin Henderson
#recover par files.
import os


'''
* pulled from the original script
'''
def findAllFilesOfType(fileExt): #pulled from original script
	logging.debug("def: findAllFilesOfType")
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
parList = []

parList = findAllFileOfType("par")

for fileName in parList:
	print fileName
