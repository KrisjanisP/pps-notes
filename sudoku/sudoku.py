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

# TODO: check for identical number in square
def ok(row, col, num) -> bool:
    for i in range(0,9):
        if sudoku[row][i] == num:
            return False
    for i in range(0,9):
        if sudoku[i][col] == num:
            return False
    
    return True
 
def place(row, col, num):
    sudoku[row][col] = num
 
def unplace(row, col):
    sudoku[row][col] = 0
    
def solve_cell(row,col) -> bool:
    if col == 9:
        row+=1
        col=0
    if row == 9 and col == 0:
        return True
    if sudoku[row][col] != 0:
        return solve_cell(row,col+1)
    for num in range(1,10):
        if ok(row,col,num):
            place(row,col,num)
            result = solve_cell(row,col+1)
            if result == True:
                return True
            unplace(row,col)
    return False
            
def solve():
    solve_cell(0,0)
 
solve()
print(sudoku)
    