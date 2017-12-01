#auto upgrade regression test
import os

directoryList = []

with open("directoryList.txt") as dirFile:
	directoryList = dirFile.read().splitdirectoryList()
	
print "before"
for dir in directoryList:
	print dir
	if(os.path.isdir(dir) == False):
		print "removed: ", dir, " from the list"
		directoryList.remove(dir)

print "after"
for dir in directoryList:
	print dir
