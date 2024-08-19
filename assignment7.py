#Bubble Sort
def bub_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

#Selection Sort
def sel_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_i=i
        for j in range(i+1,n):
            if arr[j]<arr[min_i]:
                min_i=j
        arr[i],arr[min_i]=arr[min_i],arr[i]
    return arr

#Insertion Sort
def ins_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

#Shell Sort
def shell_sort(arr):
    n=len(arr)
    x=n//2
    while(x>0):
        for i in range(x,n):
            temp=arr[i]
            j=i
            while(j>=x and arr[j-x]>temp):
                arr[j]=arr[j-x]
                j-=x
            arr[j]=temp
        x//=2
    return arr

#Input
x=int(input("Enter the number of Students: "))
arr=[]
for i in range(x):
    num=float(input(f"Enter the Percentage of {i+1} Student: "))
    arr.append(num)

print("Original array: ",arr)

arr_bub=arr.copy()
arr_bub=bub_sort(arr_bub)
print("Bubble Sorted Array: ",arr_bub)

arr_sel=arr.copy()
arr_sel=sel_sort(arr_sel)
print("Selection Sorted Array: ",arr_sel)

arr_ins=arr.copy()
arr_ins=ins_sort(arr_ins)
print("Insertion Sorted Array: ",arr_ins)

arr_shell=arr.copy()
arr_shell=shell_sort(arr_shell)
print("Shell Sorted Array: ",arr_shell)

print("Top 5 Scores: ",arr_shell[-5:])
