def LinearSearch(a,key,size):
    flag=0
    for i in range(size):
        if a[i]==key:
            flag=1
            pos=i+1
            break
    if flag==1:
        print("Key found at position", pos)
    else:
        print("Key not found")


a=[]
size=int(input("Enter the size of your list"))
for i in range(size):
    value=int(input("Enter the value in your list"))
    a.append(value)
key=int(input("Enter the key that you want to search"))
LinearSearch(a,key,size)