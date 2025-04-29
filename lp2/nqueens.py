# 🔹 N-Queens Problem – Code Explanation in Points
# This code solves the N-Queens problem, which is to place N queens on an N×N chessboard so that no two queens threaten each other (i.e., no two queens share the same row, column, or diagonal).

# 🔸 Key Concepts & Functions
# printSolution(board, N)

# Prints a single board configuration (solution).

# 1 represents a queen, 0 means empty.

# isSafe(board, row, col, N)

# Checks if placing a queen at (row, col) is safe:

# No queen in the same row on the left.

# No queen in the upper left diagonal.

# No queen in the lower left diagonal.

# solveNQUtil(board, col, N, solutions)

# Recursive backtracking function.

# Tries placing queens column by column.

# If it reaches column N, a valid solution is found and added to solutions.

# Backtracks after exploring each possibility.

# solveNQ(N)

# Initializes board and solution list.

# Calls the recursive solver.

# Prints all solutions or states that none exist.

# 🔸 Output
# Prompts for N (number of queens).

# Prints all valid arrangements (if any).

# Also prints total number of solutions found.

# 🔸 Example (N = 4)
# Output:

# yaml
# Copy
# Edit
# Total solutions found: 2
# 0 0 1 0 
# 1 0 0 0 
# 0 0 0 1 
# 0 1 0 0 

# 0 1 0 0 
# 0 0 0 1 
# 1 0 0 0 
# 0 0 1 0 
# Each 1 indicates a queen’s position.

# 🔸 Time Complexity
# Worst Case: O(N!) due to the nature of backtracking.

# Space: O(N²) for board storage.

# Let me know if you'd like a diagram or dry run to visualize it better.

def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col, N, solutions):
    if col >= N:
        solutions.append([row[:] for row in board])  # Store the solution
        return

    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            solveNQUtil(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack

def solveNQ(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solveNQUtil(board, 0, N, solutions)

    if not solutions:
        print("Solution does not exist")
    else:
        print(f"Total solutions found: {len(solutions)}")
        for solution in solutions:
            printSolution(solution, N)
            print("")

# Driver code
N = int(input("Enter the number of Queens (N): "))
solveNQ(N)
