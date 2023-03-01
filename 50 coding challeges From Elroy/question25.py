print("First Array")
def firstArray():
    max=int(input("enter the number of elements to put: "))
    # i=0
    array=[]
    for i in range(0,max):
        number=int(input("enter number: "))
        array.append(number)
    print(array)
# firstArray()

print("Second Array")
def secondArray():
    max=int(input("enter the number of elements to put: "))
    # i=0
    array=[]
    for i in range(0,max):
        number=int(input("enter number: "))
        array.append(number)
    print(array)
# secondArray()

def check():
    # first=firstArray()
    # second=secondArray()
    print(firstArray())
    # print(second)
    list=[]
    for i in range(len(firstArray())):
        if i in firstArray():
            pass
        list.append(i)

    for j in range(len(secondArray())):
        if j in secondArray():
            pass
        list.append(j)
check()