def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat


def print_mat(mat):
    for i in range(4):
        for j in range(4):
            print(mat[i][j], end=' ')
        print()
