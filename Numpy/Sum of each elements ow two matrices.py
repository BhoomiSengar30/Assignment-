#3rd matrix by user input value
import numpy as np 
n=int(input("enter the number of element you want:"))
l=list(map(int,input("enter the element: ").split()))[:n]
arr=np.array([l],dtype="i").reshape(3,3)
print(arr,np.ndim(arr),np.shape(arr))
print(np.sum(arr))


