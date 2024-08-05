#Sparse Matrix Input Func
def spr_mat(m,n):
    spr=[[m,n,0]]
    c=0
    for i in range(m):
        for j in range(n):
            val=int(input(f"Enter the A{i}{j} element: "))
            if (val!=0):
                x=[i,j,val]
                c+=1
        spr.append(x)
    spr[0][2]=c
    return spr

#Simple Transpose
def simple_trans(spr_mat):
    mt_mat=[]
    mt_mat.append([spr_mat[0][1],spr_mat[0][0],spr_mat[0][2]])
    for i in range(spr_mat[0][1]):
        for j in range(1,spr_mat[0][2]):
            if(i==spr_mat[i+1][1]):
                mt_mat.append([spr_mat[j][1],spr_mat[j][0],spr_mat[j][2]])
    return mt_mat

m=int(input("Enter number of Rows: "))
n=int(input("Enter number of Columns: "))
mat=spr_mat(m,n)
print(mat)
