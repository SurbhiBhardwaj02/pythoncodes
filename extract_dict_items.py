dict={'key':'value', 'key1':'value1', 'key2':'value2', 'key3':'value3'}
x,y= list(dict.items())[0]
print(x,y)
x,y=list(dict.items())[2]
print(x,y)

d={'k':'s'}
(c1,c2),=d.items()
print(c1)
print(c2)