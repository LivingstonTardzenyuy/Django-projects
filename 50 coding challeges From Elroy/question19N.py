def primeCompare(array,n):
    for i in array:
        if n<i:
            if i%2==0:
                pass
            else:
                return i
        else:
            pass
    

arra=[1,2,3,4,5,6,7,8,9]
print(primeCompare(arra,3))