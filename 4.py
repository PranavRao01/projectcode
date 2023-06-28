f1=open("in2.txt","r")
content1=f1.readlines()
names=[]
dob=[]
print(content1)
for i in range(0,5,1):
    line1=content1[i].replace("\n","")
    list1=line1.split(",")
    names.append(list1[0])
    list2=list1[1].split("-")
    year1=int(list2[0])
    month1=int(list2[1])
    date1=int(list2[2])
    mydate=[year1,month1,date1]
    dob.append(mydate)
print(names)    
print(dob)    

print(dob[0][0])


