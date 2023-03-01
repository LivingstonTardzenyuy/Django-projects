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

def addTwoArray():
    first=firstArray()
    second=secondArray()

    add=[]
    for i in len(first):
        add.append(i)
    for i in len(second):
        add.append(i)
    print(add)
addTwoArray()