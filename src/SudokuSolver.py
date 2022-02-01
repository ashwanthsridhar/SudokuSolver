from dokusan import generators
import numpy

'''
Created on Dec 25, 2021
@author: Ashwanth Sridhar
'''

rank = 10 #difficulty can be updated here
arr_list = list(str(generators.random_sudoku(avg_rank=rank))) # generates list of 81 strings of numbers

for i in range(len(arr_list)):
    arr_list[i] = int(arr_list[i]) # changes each string to an integer value
    
array = numpy.reshape(arr_list, (9,9)) # resizes the list of now ints into a 9x9 matrix



board = array # saves the resized matrix into another variable
print("This is the incomplete Sudoku board!") 
print(numpy.matrix(board)) # prints the board
print() # prints a blank line

"""
This helper function takes in 3 parameters (the row, column, and number to be tested).
With the parameters, it checks if the number to be tested has been used in the row, column, and
its appropriate square and returns true if all of the qualifications are met.
"""
def works(row, column, num):
    global board
    # is the tested in the row?
    # checks by keeping row constant and iterating through columns
    for i in range(0,9):
        if board[row][i] == num:
            return False
    # is the tested number in the column?
    # checks by keeping column constant and iterating through rows
    for j in range(0,9):
        if board[j][column] == num:
            return False
    # is the tested number in the square
    rowSquare = row // 3 # checks which square the row correlates to
    colSquare = column // 3 # checks which square the column correlates to
    
    for i in range(rowSquare * 3, (rowSquare * 3) + 3):
        for j in range(colSquare * 3, (colSquare * 3) + 3):
            if board[i][j] == num: # checks if selected value is within the associated square
                return False
    return True


"""
This function actually solves the sudoku board using a recursive backtracking algorithm
"""
def solve():
    global board
    for row in range(0,9):
        for column in range(0,9):
            if board[row][column] == 0: # if the board has a 0 at this spot, change the value of it
                for i in range(1, 10):
                    if works(row, column, i): #checks values 1-9 in the spot
                        board[row][column] = i 
                        solve() # if a valid number works, solve the next step
                        board[row][column] = 0 # place 0 if current solution cannot work
                return
    print("This is a possible solution to the board!")
    print(numpy.matrix(board))
    

solve()

    
    
