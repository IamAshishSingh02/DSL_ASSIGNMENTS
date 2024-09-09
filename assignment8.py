#Radix Sort using Bucket Sort
def rad_sort1(arr,n):
    bkts=[[] for _ in range(10)]
    maxi=max(arr)
    d=0
    while(maxi>0):
        maxi//=10
        d+=1
    mult=1
    while(d>0):
        for i in range(n):
            x=int(arr[i]//mult)%10
            bkts[x].append(arr[i])
        mult*=10
        j=0
        for i in range(10):
            while(len(bkts[i])>0):
                arr[j]=bkts[i].pop(0)
                j+=1
        d-=1
    return arr
    
# Radix Sort using Counting Sort
def rad_sort2(arr,n):
    maxi=max(arr)
    d=0
    while maxi>0:
        maxi//=10
        d+=1
    mult=1
    for _ in range(d):
        ct_arr=[0]*10
        for i in range(n):
            x=int(arr[i]//mult)%10
            ct_arr[x]+=1
        for i in range(1,10):
            ct_arr[i]+=ct_arr[i-1]
        arr1=[0]*n
        for i in range(n-1,-1,-1):
            x=int(arr[i]//mult)%10
            arr1[ct_arr[x]-1]=arr[i]
            ct_arr[x]-=1
        arr=arr1
        mult*=10
    return arr

#Input
n=int(input("\nEnter the number of Students: "))
print("\n")
arr=[]
for i in range(n):
    num=float(input(f"Enter the Percentage of {i+1} Student: "))
    arr.append(num)

print("\nOriginal array: ",arr)

rad1_arr=arr.copy()
rad1_arr=rad_sort1(rad1_arr,n)
print("\nRadix Sort using Bucket Sort: ",rad1_arr)

rad2_arr=arr.copy()
rad2_arr=rad_sort2(rad2_arr,n)
print("Radix Sort using Counting Sort: ",rad2_arr)

#Top 5 Scores
print("\nTop 5 Scores: ",rad2_arr[-5:])
