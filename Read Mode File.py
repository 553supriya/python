fp1=open("Cse.text","r")
if fp1:
    print("File is opened successsfully")
    fp1.seek(10,0)
    for i in fp1:
        print(i)
    '''content=fp1.raed()
    print(content)
    content=fp1.readline    
content=fp1.read(5)
print(content)
    fp1.close()