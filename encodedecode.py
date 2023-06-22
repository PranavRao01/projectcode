
s1= "i am going to the airport"
def encode():
    len1=len(s1)
    list1=[]
    for i in range(0,len1,1):
        list1.append(str(ord(s1[i])))
    n1="".join(list1)    
    print(list1)
    print(n1)
encode()
