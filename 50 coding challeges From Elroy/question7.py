def sumOfEvenNumbersInRange(min,max):
    while min<max:
        sum=0
        if min%2==0:
            sum+=min
        min+=1
        print(sum)
sumOfEvenNumbersInRange(10,30)
