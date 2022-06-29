def odd_product(num):
    for i in range(len(num)):
        for j in range (len(num)):
            if i!=j:
                pro= num[i]*num[j]
                if pro & 1:
                    return True
    return False

dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))
