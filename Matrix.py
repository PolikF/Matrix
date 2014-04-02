A=[[1.0,2.0,3.0],
   [4.0,5.0,6.0],
   [7.0,8.0,9.0]]
I=[[1.0,0.0,0.0],
   [0.0,1.0,0.0],
   [0.0,0.0,1.0]]
J=[[0.0,0.0,1.0],
   [0.0,1.0,0.0],
   [1.0,0.0,0.0]]
#print(A)
#print(I)
def matrixPrint(M,name):
    print("Matrix "+name)
    for line in M:
        print(line)

matrixPrint(A,"A") 
matrixPrint(I,"I")

def matrixAdd(A, B):
    R=[]
    for i in range(len(A)):
        line=[]
        for j in range(len(A[i])):
            line.append(A[i][j]+B[i][j])
        R.append(line)  
    return R 
matrixPrint(matrixAdd(A,I),"A+I")

def matrixZero(w,h):
    R=[]
    for _ in range(h):
        line = []
        for _ in range(w):
            line.append(0.0)
        R.append(line)
    return R
matrixPrint(matrixZero(5,5),"b")    
def matrixIdentity(s):
    R=[]
    for i in range(s):
        line = []
        for j in range(s):
            if(i == j):
                line.append(1.0)
            else:
                line.append(0.0)
        R.append(line)
    return R
matrixPrint(matrixIdentity(7),"b")  
matrixPrint(matrixZero(5,5),"b")

    
def matrixIdentityDH(s):
    R=[]
    for i in range(s):
        line = []
        for j in range(s):
            (0.0,1.0)(i == j)
        R.append(line)
    return R,
matrixPrint(matrixIdentity(7),"b") 

def matrixTranspose(A):
    R=[]
    for i in range(len(A[0])):
        line=[]
        for j in range(len(A)):
            line.append(A[j][i])
        R.append(line)
    return R
matrixPrint(matrixTranspose(A),"Matrix TA")

def matrixMultiply(A,B):
    R=[]
    for i in range(len(A)):
        line=[]
        for j in range(len(B[0])):
            s=0.0
            for k in range(len(A[0])):
                s+=A[i][k]*B[k][j]
            line.append(s)
        R.append(line)
    return R
matrixPrint(matrixMultiply(A,J),"Matrix A*J")
matrixPrint(matrixMultiply(J,A),"Matrix J*A")  
def matrixRotate(A):
    R=[]
    for i in range(len(A[0])):
        line=[]
        for j in range(len(A)):
            line.append(A[j][i])
        R.append(line)
    return R
matrixPrint(matrixTranspose(A),"Matrix TA")