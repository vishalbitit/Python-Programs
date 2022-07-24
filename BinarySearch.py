def BinarySearch(a,size,key):
    flag=0
    start=0
    end=size-1
    while start<=end and flag==0:
        mid=(start+end)//2
        if a[mid]==key:
            flag=1
            pos=mid+1
        if a[mid]<key:
            start=mid+1
        if a[mid]>key:
            end=mid-1
    if flag==1:
        print("Key found at ", pos)
    else:
        print("Key not found")
a=[]
size=int(input("Enter the size of list"))
for i in range(size):
    val=int(input("Enter the value for your list"))
    a.append(val)
key=int(input("Enter the key that you want to search"))
BinarySearch(a,size,key)