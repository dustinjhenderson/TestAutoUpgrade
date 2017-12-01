#auto upgrade regression test
import os
import subprocess

directoryList = []
failBool = False

def directoryLogic():
	print "\n"
	print os.getcwd()
	subDirs = os.listdir(".")
	for subSubDir in subDirs:
		print subSubDir
		if((".par" in subSubDir) == False):
			if(("." in subSubDir) == True):
				print "rm ", subSubDir
				up.cmdOut = subprocess.check_output(("rm ", subSubDir), shell=True)
			else:
				print "rm -rf ", subSubDir
				up.cmdOut = subprocess.check_output(("rm -rf ", subSubDir), shell=True)

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