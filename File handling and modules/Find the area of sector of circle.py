import numpy as py
pi=22/7
deg=int(input("enter the angle:"))
r=int(input("enter the radius:"))
print("here is your area of sector:")
rd=py.deg2rad(deg)
area=1/2*(r**2*rd)
print(area)
