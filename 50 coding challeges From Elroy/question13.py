def findMaxNumber():
    
    for i in range(len(array)):
        max=array[0]
        if array[i+1]>max:
            max=array[i+1]

        print (max)
array=[2,4,6,-2,5,-9,2,-10,4,20]
findMaxNumber()