def main():
    '''#open a file
    myfile=open("harini.txt","w+")
    #wrie lines in file
    myfile.write("Harini is good girl")
 '''   
    myfile=open("textfile.txt","r")
    if myfile.mode=='r':
        contents = myfile.read()
        
if __name__=="__main__":
    main()
        
