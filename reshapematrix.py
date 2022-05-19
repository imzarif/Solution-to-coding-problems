def reshape(mat, r, c):
    output = []
    flat_mat = []
    temp = []
    mat_row = len(mat)
    mat_col = len(mat[0])
    if mat_row*mat_col!=r*c:
        return mat
    for i in range(mat_row):
        for j in range(mat_col):
            flat_mat.append(mat[i][j])
   # print(flat_mat)
    i = 0
    pointer = 0
    while pointer < len(flat_mat):
        while i<c:
            temp.append(flat_mat[pointer])
            pointer += 1
            i+=1
        output.append(temp)
        temp = []
        i = 0



    return output

mat = [[1, 2], [3, 4]]
r = 4
c= 1
print(reshape(mat,r,c))











































































































