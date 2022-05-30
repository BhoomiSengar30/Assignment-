def last_line(f_name,n):
    # with open(f_name) as f:
    f=open(f_name)
    for i in (f.readlines()[-n:]):
        print(i,end="")
last_line("sample.txt",)            
