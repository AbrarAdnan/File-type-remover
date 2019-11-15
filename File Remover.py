# Import the os module, for the os.walk function
import os
found=0
# Set the directory you want to start from
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        if (fname.endswith('.o') or fname.endswith('.class') or
                fname.endswith('.obj')):
            path=os.path.join(dirName,fname)
            print(path)
            found=found+1
            try:
                os.remove(path)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
print(found) # shows total number of files deleted
