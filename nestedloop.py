f2= open("nestedloop.txt","w")
f2.write("pranav")
f2.close()
for j in range(3,6,1):
    for i in range(1,11,1):
        print(j,i,j*i)
    print("\n")
