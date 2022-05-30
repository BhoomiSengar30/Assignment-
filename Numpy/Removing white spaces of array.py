import numpy as np
arr=np.array(["akash","rathore","course"],dtype="str")
print("Original array:",arr)
x=np.char.rstrip(arr)
print(x)
