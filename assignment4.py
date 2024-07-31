def inputPoly(name):
    degree=int(input("Degree of "+name+ ": "))
    poly=[]
    for i in range(degree+1):
        coeff=float(input("Coefficient of x^" +str(i)+": "))
        poly.append(coeff)
    return poly

def printPoly(poly,n):
    for i in range(n-1,-1,-1):
        if poly[i]!=0:
            if poly[i]>0 and i!=n-1:
                print(" + ",end="")
            if poly[i]<0:
                print(" - ",end="")
            if abs(poly[i])!=1 or i==0:
                print(abs(poly[i]),end="")
            if i!=0:
                print("x",end="")
                if i != 1:
                    print("^",i,end="")
    print()

print("Enter coefficients of polynomial A")
A=inputPoly("A")
print("\nEnter coefficients of polynomial B")
B=inputPoly("B")

m=len(A)
n=len(B)

print("\nA is: ")
printPoly(A,m)
print("B is: ")
printPoly(B,n)

#Addition
def add(A,B,m,n):
    size=max(m,n)
    sum=[0]*size
    for i in range(m):
        sum[i]=A[i]
    for i in range(n):
        sum[i]+=B[i]
    return sum

sum=add(A,B,m,n)
size=max(m,n)
print("\nSum of A & B is: ")
printPoly(sum,size)

#Multipication
def multiply(A,B):
    m=len(A)
    n=len(B)
    product=[0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            product[i+j]+=A[i]*B[j]
    return product

product=multiply(A,B)
print("Product of A & B is: ")
printPoly(product,size)
