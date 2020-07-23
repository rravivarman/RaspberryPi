import time

def moveFTPFiles(serverName,userName,passWord,remotePath,localPath,deleteRemoteFiles=False,onlyDiff=False):
	"""Connect to an FTP server and bring down files to a local directory"""
	import os
	#from sets import Set
	from ftplib import FTP
	try:
		ftp = FTP(serverName)
	except:
		print ("Couldn't find server")
	ftp.login(userName,passWord)
	#ftp.cwd(remotePath)
	
	try:
		print ("Connecting...")
		if onlyDiff:
			lFileset = set(os.listdir(localPath))
			rFileset = set(ftp.nlst())
			transferList = list(rFileset - lFileset)
			print ("Missing: " + str(len(transferList)))
		else:
			transferList = ftp.nlst()
		delMsg = ""	
		filesMoved = 0
		for fl in transferList:
			# create a full local filepath
			localFile = localPath + fl
			grabFile = True
			if grabFile:				
				#open a the local file
				fileObj = open(localFile, 'wb')
				# Download the file a chunk at a time using RETR
				ftp.retrbinary('RETR ' + fl, fileObj.write)
				# Close the file
				fileObj.close()
				filesMoved += 1
				
			# Delete the remote file if requested
			if deleteRemoteFiles:
				ftp.delete(fl)
				delMsg = " and Deleted"
			
		print ("Files Moved" + delMsg + ": " + str(filesMoved) + " on " + timeStamp())
	except:
		print ("Connection Error - " + timeStamp())
	ftp.close() # Close FTP connection
	ftp = None

def timeStamp():
    """returns a formatted current time/date"""
    import time
    return str(time.strftime("%a %d %b %Y %I:%M:%S %p"))

#if __name__ == '__main__':

#--- constant connection values
ftpServerName = "swathi.dreamerindia.com"
ftpU = "swathi"
ftpP = "Admin@123"
remoteDirectoryPath = "remote/ftp/subdirectory"
localDirectoryPath = "/home/pi/images/"#"""local\sub\directory"""
deleteAfterCopy = False         #set to true if you want to clean out the remote directory
onlyNewFiles = True                     #set to true to grab & overwrite all files locally

while 1:
	print ("\n-- Retreiving Files----\n")
	moveFTPFiles(ftpServerName,ftpU,ftpP,remoteDirectoryPath,localDirectoryPath,deleteAfterCopy,onlyNewFiles)
	time.sleep(23)
