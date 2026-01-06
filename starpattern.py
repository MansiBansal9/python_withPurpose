n=int(input("enter no of rows\t"))
ch=int(input("enter 0 or 1\t"))

if ch==0:
    ch=False
elif ch==1:
    ch=True
if ch==True:
    for i in range (1,n+1):
        print("*"*i)
elif ch==False:
    for i in range (n,0,-1):
        print("*"*i)
