d1={1:2,2:3,4:5}
d2={9:8,8:7,7:6}
d3=d1.copy()
d3.update(d2)
print(d3)
# second method of merging two dictioneries in to one
d1={1:2,2:3,4:5}
d2={9:8,8:7,7:6}
d3={**d1,**d2}
print(d3)


  
