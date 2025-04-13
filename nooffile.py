import os 
def file_info():
    totalbytes = 0
    folder ="deps"
    #get a list of all the files in current directory
    dirlist = os.listdir(folder)
    for entry in dirlist:
        #make sure it's file!
        if os.path.isfile(folder + "/" + entry)and entry.endswith(".txt"):
            #add the file size to the total
            filesize = os.path.getsize(folder + "/" + entry)
            totalbytes += filesize
    return totalbytes

result = Answer.file_info()
