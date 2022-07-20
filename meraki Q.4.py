a=int(input("enter the num"))
b=int(input("enter the num"))
c=int(input("enter the num"))
if a>b and a>c:
    print(a,"is greatest")
elif b>c and b>a:
    print(b,"is greatest")
else:
    print(c,"is greatest")