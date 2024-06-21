'''
open()
Create()
Read()
ReadLine()
Write()
WeiteLine()
Fseek()
FTell()
Close()
'''
fp=open("Cse.txt","w")
if fp:
    print("file is created successfully")
fp.write("Hi students wellcome to cmrec\n today is Friday")
fp.writelines("Hi students wellcome to cmrec\n today is Friday\n hello world")

fp.close()