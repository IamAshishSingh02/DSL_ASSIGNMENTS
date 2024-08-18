#Sparse Matrix Input Function
def spr_mat(m,n):
    spr=[[m,n,0]]
    c=0
    for i in range(m):
        for j in range(n):
            val=int(input(f"Enter the A[{i}][{j}] element: "))
            if (val!=0):
                x=[i,j,val]
                spr.append(x)
                c+=1
    spr[0][2]=c
    return spr

#Simple Transpose
def simple_trans(spr_mat):
    mt_mat=[]
    mt_mat.append([spr_mat[0][1],spr_mat[0][0],spr_mat[0][2]])
    for i in range(spr_mat[0][1]):
        for j in range(1,spr_mat[0][2]+1):
            if(i==spr_mat[j][1]):
                mt_mat.append([spr_mat[j][1],spr_mat[j][0],spr_mat[j][2]])
    return mt_mat

#Fast Transpose
def fast_trans(spr_mat):
    ft_mat=[[spr_mat[0][1],spr_mat[0][0],spr_mat[0][2]]]
    count=[0]*spr_mat[0][1]
    index=[0]*(spr_mat[0][1]+1)
    for i in range(1,spr_mat[0][2]+1):
        count[spr_mat[i][1]]+=1
    index[0]=1
    for i in range(1,spr_mat[0][1]+1):
        index[i]=index[i-1]+count[i-1]
    for i in range(1,spr_mat[0][2]+1):
        ft_mat.append([0,0,0])
    for i in range(1,spr_mat[0][2]+1):
        ft_mat[index[spr_mat[i][1]]]=[spr_mat[i][1],spr_mat[i][0],spr_mat[i][2]]
        index[spr_mat[i][1]]+=1
    return ft_mat

#Addition of two Sparse Matrices
def add_sparse(mat1,mat2):
    add_mat=[[mat1[0][0],mat1[0][1],0]]
    i=1
    j=1
    while(i<=mat1[0][2] and j<=mat2[0][2]):
        if(mat1[i][0]==mat2[j][0]):
            if(mat1[i][1]==mat2[j][1]):
                add_mat.append([mat1[i][0],mat1[i][1],mat1[i][2]+mat2[j][2]])
                i+=1
                j+=1
            elif(mat1[i][1]<mat2[j][1]):
                add_mat.append([mat1[i][0],mat1[i][1],mat1[i][2]])
                i+=1
            else:
                add_mat.append([mat2[j][0],mat2[j][1],mat2[j][2]])
                j+=1
        elif(mat1[i][0]<mat2[j][0]):
            add_mat.append([mat1[i][0],mat1[i][1],mat1[i][2]])
            i+=1
        else:
            add_mat.append([mat2[j][0],mat2[j][1],mat2[j][2]])
            j+=1
    while(i<=mat1[0][2]):
        add_mat.append([mat1[i][0],mat1[i][1],mat1[i][2]])
        i+=1
    while(j<=mat2[0][2]):
        add_mat.append([mat2[j][0],mat2[j][1],mat2[j][2]])
        j+=1
    add_mat[0][2]=len(add_mat)-1
    return add_mat

m=int(input("Enter number of Rows: "))
n=int(input("Enter number of Columns: "))
print("\n")
mat=spr_mat(m,n)

print("\nSparse Matrix:")
print(mat)

print("\nSimple Transpose:")
print(simple_trans(mat))

print("\nFast Transpose:")
print(fast_trans(mat))

print("\nAddition of two Sparse Matrices")
print("Give values of Matrix2")
mat2=spr_mat(m,n)

print("\nSparse Matrix 2:")
print(mat2)

print("\nAddition:")
print(add_sparse(mat,mat2))
