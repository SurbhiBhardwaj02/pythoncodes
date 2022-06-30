def maxmin(num):
    n=num[0]
    max=0
    min=0
    for i in num:
        if i>n:
            max=i
        elif i<n:
            min=i
    return max , min

print(maxmin([8,5,19,29,3,7]))






    