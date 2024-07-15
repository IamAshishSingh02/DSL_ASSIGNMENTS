def union(x,y):
    r=x.copy()
    for i in y:
        if(i not in r ):
            r.append(i)
    
    return r

def intersection(x,y):
    r=[]
    for i in x:
        if(i in y):
            r.append(i)
    
    return r

def subtract(x,y):
    r=[]
    for i in x:
        if(i not in y):
            r.append(i)

    return r

n=int(input("Enter Total number of Students: "))
a=[]
b=[]
c=[]

cric=int(input("Enter Number of students who play Cricket: "))
print("Enter Roll number's of students who play Cricket: ")
for i in range(cric):
    x=int(input())
    a.append(x)

baddy=int(input("Enter Number of students who play Badminton: "))
print("Enter Roll number's of students who play Badminton: ")
for i in range(baddy):
    x=int(input())
    b.append(x)

socc=int(input("Enter Number of students who play Football: "))
print("Enter Roll number's of students who play Football: ")
for i in range(socc):
    x=int(input())
    c.append(x)

print("The Required list are:")
print("Cricket: ",a)
print("Badminton: ",b)
print("Football: ",c)

print("Students who play both Cricket and Badminton: ",intersection(a,b))
print("Students who play either Cricket or Badminton but not both: ", subtract(union(a,b),intersection(a,b)))
print("Students who play neither Cricket nor Badminton: ",n-len(union(a,b)))
print("Students who play  Cricket and Football but not Badminton: ",len(union(union(a,b),c))-len(c))
print("Students who do not play any game: ",n-len(union(c,union(a,b))))
print("Students who play at least one game: ",union(union(a,b),c))
print("Students who play all the games: ",intersection(c,intersection(a,b)))