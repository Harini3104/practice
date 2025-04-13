import os
from os import path
import shutil
from shutil import make_archive
def main():
    #make a duplicate copy
    if path.exists("textfile.txt"):
        src=path.realpath("textfile.txt")
    #make backup copy app "bak"
    dst=src+".bak" 
    shutil.copy(src,dst)
    #rename the file
    os.rename("textfile.txt","hag.txt")
    #put things into put file
    root_dir, tail = path.split(src)

if __name__ == "__main__":
    main() 