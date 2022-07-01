#Write a python program to convert decimal to hexadecimal.
def convertt(num):
    str1=''   #str1 is character

    x=num%16
    if x<10:
        str1=x
    if x==10:
        str1='A'
    elif x==11:
        str1='B'
    elif x==12:
        str1='C'
    elif x==13:
        str1='D'
    elif x==14:
        str1='E'
    elif x==16:
        str1='F'

    if (num-x)!=0:
        return convertt(num//16)+str(str1)

    else:
        return str(str1)
    
num=[775,1256]
print({convertt(x) for x in num})
    

#    OR

m=654
print(format(m,'02x'))
    