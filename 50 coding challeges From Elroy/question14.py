def displayFibNumber(n):
    result=0
    for i in range(10):
        for j in range (i+1):
            result+=i+j
    print(result)

displayFibNumber(10)