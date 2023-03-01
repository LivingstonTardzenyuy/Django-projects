def sumOfNumbers(min,max):
    sum=0
    while min<max:
        sum+=min
        min+=1
    print(sum)
sumOfNumbers(1,10)