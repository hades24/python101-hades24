largest = None
smallest = None
a=[]
n=10

while True:
    for i in range(0,n):
        l=input("enter the number \n")
        a.append(l)
        if l == "done":
            break
        if a[i]>a[i+1]:
            largest=i
        else:
            a[i]=a[i+1]
        if a[i]<a[i+1]:
            smallest = i
        else:
            a[i]=a[i+1]
    print("largest = ",largest)
    print("smallest : ",smallest)