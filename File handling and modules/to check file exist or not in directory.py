import os
filename=input("enter the file name:")
if os.path.isfile(filename):   
      f=open(filename)
      print(f)
      f.close()
else:
    print("file is not found")      
