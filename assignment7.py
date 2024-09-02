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
    g=n//2
    while(g>0):
        for i in range(g,n):
            tmp=arr[i]
            j=i
            while(j>=g and arr[j-g]>tmp):
                arr[j]=arr[j-g]
                j-=g
            arr[j]=tmp
        g//=2
    return arr

#Input
x=int(input("\nEnter the number of Students: "))
print("\n")
arr=[]
for i in range(x):
    num=float(input(f"Enter the Percentage of {i+1} Student: "))
    arr.append(num)

print("\nOriginal array: ",arr)

arr_bub=arr.copy()
arr_bub=bub_sort(arr_bub)
print("\nBubble Sorted Array: ",arr_bub)

arr_sel=arr.copy()
arr_sel=sel_sort(arr_sel)
print("Selection Sorted Array: ",arr_sel)

arr_ins=arr.copy()
arr_ins=ins_sort(arr_ins)
print("Insertion Sorted Array: ",arr_ins)

arr_shell=arr.copy()
arr_shell=shell_sort(arr_shell)
print("Shell Sorted Array: ",arr_shell)

#Top 5 Scores
print("\nTop 5 Scores: ",arr_bub[-5:])          
