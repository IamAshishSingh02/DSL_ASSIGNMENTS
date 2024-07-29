#Addition of Polynomials
def input_polynomial():
    degree = int(input("Enter the degree of the polynomial: "))
    coefficients = []
    for i in range(degree, -1, -1):
        coeff = float(input(f"Enter the coefficient of x^{i}: "))
        coefficients.append(coeff)
    return coefficients

def print_polynomial(coefficients):
    degree = len(coefficients) - 1
    print("The polynomial is: ")
    for i, coeff in enumerate(coefficients):
        if coeff != 0:
            if i == 0:
                print(f"{coeff}x^{degree}", end="")
            elif i == degree:
                print(f" + {coeff}", end="")
            else:
                print(f" + {coeff}x^{degree-i}", end="")
    print()

def add_polynomials(poly1, poly2):
    max_degree = max(len(poly1), len(poly2))
    result = [0] * max_degree

    for i in range(max_degree):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]

    return result

print("Enter the first polynomial:")
poly1 = input_polynomial()
print_polynomial(poly1)

print("\nEnter the second polynomial:")
poly2 = input_polynomial()
print_polynomial(poly2)

result = add_polynomials(poly1, poly2)
print("\nThe sum of the two polynomials is:")
print_polynomial(result)