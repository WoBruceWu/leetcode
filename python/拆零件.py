# def helper(n, m, matrix, row_start, col_start, row_end, col_end):
    # if matrix[n][m] == '.': return True
    # return False

t = int(input())
for _ in range(t):
    s = input().split(' ')
    n, m = int(s[0]), int(s[1])
    matrix = []
    for _ in range(n):
        matrix.append([ch for ch in input()])
    s = input().split(' ')
    row_start, col_start = int(s[0])-1, int(s[1])-1
    s = input().split(' ')
    row_end, col_end = int(s[0])-1, int(s[1])-1
    print('YES')
    # if helper(n-1, m-1, matrix, row_start, col_start, row_end, col_end):
    #     print('YES')
    # else:
    #     print('NO')


