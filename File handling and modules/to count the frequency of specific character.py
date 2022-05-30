f=open("sample.txt")
a=f.read()
s=len(a)
c=0
for i in range(s):
    if a[i]=="a":
        c+=1 
print(c)        
