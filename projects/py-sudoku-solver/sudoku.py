sudoku = [
    [9,2,6,0,1,0,0,0,5],
    [0,0,0,3,9,0,0,0,0],
    [0,7,0,2,6,0,8,0,1],
    [0,9,7,0,0,0,0,0,0],
    [3,0,2,9,5,1,6,0,7],
    [0,6,0,0,0,0,0,1,0],
    [2,1,0,7,0,6,5,3,8],
    [0,8,0,0,2,0,4,0,9],
    [0,0,0,5,0,9,1,6,0]
]

def ok(row, col, num) -> bool:
    for i in range(0,9):
        if sudoku[row][i] == num:
            return False
    for i in range(0,9):
        if sudoku[i][col] == num:
            return False
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[(row//3)*3+i][(col//3)*3+j] == num:
                return False
    return True
 
def place(row, col, num):
    sudoku[row][col] = num
 
def unplace(row, col):
    sudoku[row][col] = 0

def next_cell(row,col) -> tuple[int,int]:
    if col == 8:
        row+=1
        col=0
    else:
        col+=1
    return (row,col)

def solve_cell(row,col) -> bool:
    if row == 9:
        return True
    if sudoku[row][col] != 0:
        return solve_cell(*next_cell(row,col))
    for num in range(1,10):
        if ok(row,col,num):
            place(row,col,num)
            result = solve_cell(*next_cell(row,col))
            if result == True:
                return True
            unplace(row,col)
    return False
            
def solve():
    solve_cell(0,0)
 
solve()
for row in sudoku:
    print(row)
    