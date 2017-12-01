#auto upgrade regression test
import os

directoryList = []
failBool = False

def directoryLogic():
	print "\n"
	print os.getcwd()
	subDirs = os.listdir(".")
	for subSubDir in subDirs:
		print subSubDir

# ------------------- main starts here -----------------
		
with open("directoryList.txt") as dirFile:
	directoryList = dirFile.read().splitlines()
	
print "before"
for dir in directoryList:
	print dir
	if(os.path.isdir(dir) == False):
		print "removed: ", dir, " from the list"
		directoryList.remove(dir)

print "after"
for dir in directoryList:
	print dir

for directory in directoryList:
	try:
		os.chdir(directory)
	except:
		print"error"
		exit()
	directoryLogic()
	
print "done"