n=str(input("enter the sentence"))
list=[]
str=""
for i in n:
    if i==" ":
        list.append(str)
        str=""
    else:
        str+=1
if str:
    list.append(str)
    print(list)
