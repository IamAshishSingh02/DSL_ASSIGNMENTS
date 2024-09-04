#Radix Sort using Bucket Sort
def rad_sort1(arr,n):
    bkts=[[],[],[],[],[],[],[],[],[],[]]
    maxi=max(arr)
    d=0

    while(maxi>0):
        maxi//=10
        d+=1

    mult=1
    while(d>0):
        for i in range(n):
            x=(arr[i]//mult)%10
            bkts[x].append(arr[i])
        mult*=10
        j=0
        for i in range(10):
            while(len(bkts[i])>0):
                arr[j]=bkts[i].pop(0)
                j+=1
        d-=1
    return arr
    
#Radix Sort using Counting Sort
def rad_sort2(arr,n):

    
    