'''
Given a N by M matrix of numbers
print out the matrix in a clockwise spiral.
'''
    
def spiralPrint(mat):
    n = len(mat)    #i = rows
    m = len(mat[0]) #j = columns
    k = 0   #represent row
    l = 0   #represnt colummn
    
    while k < n and l < m:
        for i in range(l, m):
            print(mat[k][i])
        k += 1
        for i in range(k, n):
            print(mat[i][m-1])
        m -= 1
        if (k < n):
            for i in range(m-1, l-1,-1):
                print(mat[n-1][i])
            n -= 1
        if(l < m):
            for i in range(n-1, k-1, -1):
                print(mat[i][l])
            l += 1
    
    print("")

mat = [[1,  2,  3,  4,  5],
       [6,  7,  8,  9,  10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]

a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
 
spiralPrint(mat)
spiralPrint(a)