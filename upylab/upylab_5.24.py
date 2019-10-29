def print_mat(M):
    tmp = ''
    for i in range(len(M)):
        for j in range(len(M[i])):
            tmp += str(M[i][j]) + ' '
        print(tmp)
        tmp = ''

ma_matrice = eval(input())
print_mat(ma_matrice)
