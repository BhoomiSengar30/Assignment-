def check_perfect(num):
    cpy=num
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==cpy:
        print("it is a perfect number")
    else:
        print("not perfect number")
n=int(input("enter the positive number to check perfect")) 
check_perfect(n)                   
