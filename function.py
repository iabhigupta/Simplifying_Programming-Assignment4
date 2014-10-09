import os,sys
def one():
    print "This is the first version of code."
    f_read=open('example2_2.txt','r').readlines()
    f_write=open('example2_2.txt','w')
    for eachline in f_read:
        eachline=eachline.strip()+","+"User_Name"
        f_write.write(eachline+"\n")
    f_write.close()
    return

def two():
    print "CSV file is updated with default values."
    return
   
def three():

    print "This would be final version of code"
    return
    

