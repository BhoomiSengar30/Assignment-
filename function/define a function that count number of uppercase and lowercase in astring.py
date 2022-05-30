def count(str):
    upper=0
    lower=0
    for i in range(len(str)):
        if str[i].isupper():
            upper+=1
        else:
            lower+=1
    print(upper,lower)
str=input("enter the string: ")
count(str) 
