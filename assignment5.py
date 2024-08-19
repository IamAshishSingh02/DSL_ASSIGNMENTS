#Linear Search
c=0
def linearsearch(key,a):
    global c
    for i in range(len(a)):
        c+=1
        if(a[i]==key):
            return i
    return -1

a=[]
key=int(input("Element to be Found b/w 1-100: "))
for i in range(1,100):
    a.append(i)
linearsearch(key,a)
print(f"Number of Operations in Linear Search is: {c}")

#Bianry Search
d=0
def binarysearch(key,a):
    global d
    f=0
    l=len(a)-1
    m=0
    while(f<=l):
        d+=1
        m=int(l+(f-l)/2)
        if(a[m]<key):
            f=m+1
        elif(a[m]>key):
            l=m-1
        else:
            return m
    return -1

binarysearch(key,a)
print(f"Number of Operations in Binary Search is: {d}")
if(binarysearch(key,a)==-1):
    print("Element is Not Found")

#Sentinel Search
e=0
def sentinelsearch(a,key):
    global e
    last=a[-1]
    a[-1]=key
    i=0
    while(a[i]!=key):
        i+=1
        e+=1
    a[-1]=last
    if(i<len(a)-1 or last==key):
        return i
    else:
        return -1

index = sentinelsearch(a,key)
print(f"Number of Operations in Sentinel Search: {e}")

#Fibonacci Search
f=0
def fibonacci_search(arr,x):
    global f
    fib2=0 
    fib1=1 
    fibM=fib2+fib1 
    while (fibM<len(arr)): 
        fib2=fib1 
        fib1=fibM 
        fibM=fib2+fib1 
    offset=-1 
    while(fibM>1): 
        i=min(offset+fib2,len(arr)-1) 
        f+=1
        if(arr[i]<x): 
            fibM=fib1 
            fib1=fib2 
            fib2=fibM-fib1 
            offset=i 
        elif(arr[i]>x): 
            fibM=fib2 
            fib1=fib1-fib2 
            fib2=fibM-fib1 
        else: 
            return i 
    if(fib1 and arr[offset+1]==x): 
        return offset+1 
    return -1

index=fibonacci_search(a,key)
print(f"Number of Operations in Fibonacci Search: {f}")
print(f"{key} found at index {index}")
