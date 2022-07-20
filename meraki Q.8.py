list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
i=0
j=0
b=[]
while i<len(list2):
    list1.append(list2[i])
    while j<len(list1):
        if list1[j] not in b:
            b.append(list1[j])
        j+=1
    i+=1
print(b)