import numpy as np 
x=np.array(["akash","rathore","elephantinforest","c++"],dtype=np.str)
print("original array:")
print(x)
centered=np.char.center(x,15,fillchar="_")
left=np.char.ljust(x,15,fillchar="_")
right=np.char.rjust(x,15,fillchar="_")
print("centered=",centered)
print("left=",left)
print("right=",right)
