#auto upgrade regression test
import os
import subprocess

directoryList = []
scriptFailed = False
setUpFailed = False
cmdOut = ""
clearDirs = False
launchScripts = True
parsFiles = False
logFileName = "/LOGOUT.log"

def parsInput(text):
	text = text.strip(" ")
	text = text.lower()
	if text[0] == "y":
		return True
	else:
		return False

def getOperatingInput(clearDirs, launchScripts, parsFiles):
	print "Clear Directorys in text list? (defalt no)"
	text = raw_input("y/n:\n")
	clearDirs = parsInput(text)
	print "Launch Scipts? (defalt yes)"
	text = raw_input("y/n:\n")
	launchScripts = parsInput(text)
	print "Pars log files? (defalt no)"
	text = raw_input("y/n:\n")
	parsFiles = parsInput(text)
	return clearDirs, launchScripts, parsFiles

def directoryLogic():
	print "\n"
	print os.getcwd()
	subDirs = os.listdir(".")
	for subSubDir in subDirs:
		print subSubDir
		if((".par" in subSubDir) == False):
			if(("." in subSubDir) == True):
				print "rm ", subSubDir
				cmdOut = subprocess.check_output(("rm " + subSubDir), shell=True)
			else:
				print "rm -rf ", subSubDir
				cmdOut = subprocess.check_output(("rm -rf " + subSubDir), shell=True)

def runUpgrade(directoryList, scriptDir):
	try:
		os.chdir(scriptDir)
	except:
		exit()
	for subDir in directoryList:
		print "python dustinRewrite.py --single_upgrade=" + subDir
		cmdOut = subprocess.check_output("python dustinRewrite.py --single_upgrade=" + subDir, shell=True)

def getSuccessWords():
	successKeyWords = []
	with open("successKeyWords.txt") as sucFile:
		for line in sucFile:
			successKeyWords.append(line.replace("\n", ""))
	return successKeyWords

def getFailWords():
	errorKeyWords = []
	with open("errorKeyWords.txt") as errorFile:
		for line in errorFile:
			errorKeyWords.append(line.replace("\n", ""))
	return errorKeyWords
		
def checkLogs(directoryList, logFileName, successKeyWords, errorKeyWords):
	dirNumber = 0
	passBool = False
	for dir in directoryList():
		passBool = False
		try:
			os.chdir(scriptDir)
		except:
			exit()
		try:
			with open(dir + "/" + logFileName) as log:
				for line in log:
					if successKeyWords[dirNumber] in line:
						passBool = True
						break
					if errorKeyWords[dirNumber] in line:
						passBool = False
						break
		except:
			print "failed to open log file for: ", dir
		if(passBool == True):
			print "Pass: ", dir
		else:
			print "Fail: ", dir
		dirNumber = dirNumber + 1


# ------------------- main starts here -----------------

clearDirs, launchScripts, parsFiles = getOperatingInput(clearDirs, launchScripts, parsFiles)

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
	if(clearDirs == True):
		directoryLogic()

if(launchScripts == True):
	runUpgrade(directoryList, "/data/dustinhe/designStoreScriptCopy")

checkLogs(directoryList, logFileName, successKeyWords, errorKeyWords)
	
print "done"