print ("create a half pyrimad using *")
n=int(input("Please input the amount of rows you want"))
for i in range(n):
    for j in range(i+1):
        print ("*", end="")
    print()