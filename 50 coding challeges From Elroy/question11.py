def averageNumberInArray():
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    
    average=sum/len(array)
    print(sum)
    print(average)

array=[3,67,4,34,7,4,2,67,3,23,6,3,774,65]
averageNumberInArray()