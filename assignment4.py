#Input polnomials Func
def input_poly(p):
    print(p)
    deg=int(input("\nEnter the degree of the polynomial: "))
    coeffs=[]
    for i in range(deg+1):
        c=float(input(f"Enter the coefficient of x^{i}: "))
        coeffs.append(c)
    return coeffs

#Printing Polynomials Func
def print_poly(coeffs):
    terms=[]
    for i in range(len(coeffs)):
        if coeffs[i]!=0:
            term=""
            if coeffs[i]!=1 or i==0:
                term+=str(coeffs[i])
            if i>0:
                term+="x"
                if i>1:
                    term+="^"+str(i)
            terms.append(term)
    print("+".join(reversed(terms)).replace("+ -","- "))

#Evaluating Polynomials Func
def eval(coeffs,x):
    result=0
    for i in range(len(coeffs)):
        result+=coeffs[i]*(x**i)
    return result

#Adding Polynomials Func
def add(c1,c2):
    max_len=max(len(c1),len(c2))
    result=[0]*max_len
    for i in range(max_len):
        if i<len(c1):
            result[i]+=c1[i]
        if i<len(c2):
            result[i]+=c2[i]
    return result

#Multiplying Polynomials Func
def mul(c1,c2):
    result=[0]*(len(c1)+len(c2)-1)
    for i in range(len(c1)):
        for j in range(len(c2)):
            result[i+j]+=c1[i]*c2[j]
    return result

#Taking Input from User
p1=input_poly("\nEnter the first polynomial")
p2=input_poly("\nEnter the second polynomial")

#Printing Given Polynomials
print("\nPolynomial I:")
print_poly(p1)
print("\nPolynomial II:")
print_poly(p2)

#Evaluating & Printing Polynomials at Given Value of x
x1=float(input("\nEnter the value of x to evaluate Polynomial I: "))
x2=float(input("Enter the value of x to evaluate Polynomial II: "))
print("\nPolynomial I evaluated at x=",x1,":",eval(p1,x1))
print("Polynomial II evaluated at x=",x2,":",eval(p2,x2))

#Adding & Printing Polynomials
p3=add(p1,p2)
print("\n[Polynomial I]+[Polynomial II]:")
print_poly(p3)

#Multiplying & Printing Polynomials
p4=mul(p1,p2)
print("\n[Polynomial I]X[Polynomial II]:")
print_poly(p4)
