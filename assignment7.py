#Bubble Sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

#Selection Sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

#Insertion Sort
def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

#Shell Sort
def shell_sort(arr):
    n=len(arr)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap//=2
    return arr

#Input
x=int(input("Enter the number of Students: "))
arr=[]
for i in range(x):
    num=float(input(f"Enter the Percentage of {i+1} Student: "))
    arr.append(num)

print("Original array: ",arr)

arr_bubble=arr.copy()
arr_bubble=bubble_sort(arr_bubble)
print("Bubble Sorted Array: ",arr_bubble)

arr_selection=arr.copy()
arr_selection=selection_sort(arr_selection)
print("Selection Sorted Array: ",arr_selection)

arr_insertion=arr.copy()
arr_insertion=insertion_sort(arr_insertion)
print("Insertion Sorted Array: ",arr_insertion)

arr_shell=arr.copy()
arr_shell=shell_sort(arr_shell)
print("Shell Sorted Array: ",arr_shell)

print("Top 5 Scores: ",arr_shell[-5:])
