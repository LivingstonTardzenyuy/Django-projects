def multiplicationTable():
    for i in range(12):
        for j in range(0,10):
            print(str(i) +"*" +str(j)+ "=" + str(i*j))
        print("mulitiplication table of"+ str(i+1))
multiplicationTable()