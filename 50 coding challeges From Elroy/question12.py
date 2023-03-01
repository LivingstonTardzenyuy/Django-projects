def returnONlyPostiveNumbers():
    tempArray=[]
    for i in range(len(array)):
        if array[i]>0:
            tempArray.append(array[i])
        else:
            pass
    print(tempArray)
array=[2,4,6,-2,5,-9,2,-10,4,20]
returnONlyPostiveNumbers()