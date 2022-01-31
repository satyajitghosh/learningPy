board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

initialHashT = {}
for i in range(9):
    initialHashT[i] = False

rows = [initialHashT.copy() for i in range(9)]
cols = [initialHashT.copy() for i in range(9)]
sqrs = [[initialHashT.copy(),initialHashT.copy(),initialHashT.copy()],
        [initialHashT.copy(),initialHashT.copy(),initialHashT.copy()],
        [initialHashT.copy(),initialHashT.copy(),initialHashT.copy()]]

isValidSudoku = True

for i in range(9):
    for j in range(9):
        if board[i][j] != ".":
            idx = int(board[i][j]) - 1
            if not(rows[i][idx]) and not(cols[j][idx]) and not(sqrs[int(i/3)][int(j/3)][idx]):
                rows[i][idx] = True
                cols[j][idx] = True
                sqrs[int(i/3)][int(j/3)][idx] = True
            else:
                isValidSudoku = False
                break
    else:
        continue
    break

print(isValidSudoku)
