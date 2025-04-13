import os
from os import path
import datetime
from datetime import date,time,timedelta
import time
def main():
    #print os name
    print(os.name)
    #check for item existence
    print("Item exists:",(path.exists("textfile.txt")))
    print("Item is a file:",path.isfile("textfile.txt")) 
    print("Item is a dir:",path.isdir("textfile.txt")) 
    #work with file paths
    print("Item's path:",path.realpath("textfile.txt"))
    print("Item's path and name:",path.split(path.realpath("textfile.txt")))
    #    get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))  
    print(t) 
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))) 
 #how long its modified
    td=datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been",td,"since the file was modified")
    print("or,",td.total_seconds(),"seconds")
if __name__ =="__main__":
    main()