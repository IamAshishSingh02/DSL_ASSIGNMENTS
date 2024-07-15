list=[]
n=int(input("Enter the number of Students: "))

for i in range(0,n):
    i=int (input("Enter the number of marks: "))
    if(i<=50):
        list.append(i)
    else:
        print("Invalid Input\n Re-Enter the Marks: ")
        i=(int(input("Enter the Marks of Student: ")))
        list.append(i)

def absent(list):
    c=0
    for i in list:
        if(i==-1):
            c+=1
    return c

def maximum(list):
    max=list[0]
    for i in list:
        if(i>max):
            max=i
    return max

def minimum(list):
    min=list[0]
    for i in list:
        if(i<min & i!=-1):
            min=i
    return min

def sum(list):
    s=0
    for i in list:
        s+=i
    s+=absent(list)
    return s

def average(list):
    avg=(sum(list)+absent(list))/(n-absent(list))
    return avg

def frequency(list):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    for i in list:
        if(i>=0 & i<=10):
            c1+=1
        elif(i>=11 & i<=20):
            c2+=1
        elif(i>=21 & i<=30):
            c3+=1
        elif(i>=31 & i<=40):
            c4+=1
        elif(i>=41 & i<=50):
            c5+=1
        return(c1,c2,c3,c4,c5)

print("Marks of the students are: ",list)
print("Number of absent students are: ",absent(list))
print("Maximum marks are: ",max(list))
print("Minimum marks are: ",min(list))
print("Average marks of all students are: ",average(list))
print("maximum frequency of marks is:", max(frequency(list)))

        
