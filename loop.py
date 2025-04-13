x=0
#while loop
'''while(x<5):
    print(x)
    x=x+1'''
#for loop
'''for x in range(5,10):
    print(x)'''
#loop over collection
'''days=["mo,tu,we,th,fr,sa,su"]
for x in days:
        print(x)'''
 
#break and continue   
for x in range(5,10):
    if x==7:
        continue
        #break
    print(x)
#enumerate fun
days=["mo,tu,we,th,fr,sa,su"]
for i,d in enumerate(days):
        print(i, d) 
 
