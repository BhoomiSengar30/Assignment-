f=open("sample.txt","a")
for i in range(3):
    name=input("enter your name:")
    f.write(name)
    f.write("\n")
f.close()    
print("Data updeted successfully...")
    
