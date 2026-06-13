# Matrix

'''You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.'''

'''Note: 1) even number of matrix ke liye farak nahi padta ki srow<erow like but odd number ke liye 
   middle element skip ho jayega is liye srow<=erow same for column also
   2) Corner case: srow == erow and scol == ecol means only one element is left to be added, same row aue same col hoga to repeate hoga break karna h.'''

class Solution:
    def spiralOrder(self, mat):
        result = []
        if not mat:
            return result

        m = len(mat)      # number of rows
        n = len(mat[0])   # number of columns

        '''
    Example:mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]   
    mat is a list containing 3 inner lists.
    → So, len(mat) = 3 → number of rows.

    Each inner list (like mat[0] = [1, 2, 3]) represents a single row.
    → The number of elements in that row = number of columns.'''    

        # Initialize start and end indices
        srow, erow = 0, m - 1
        scol, ecol = 0, n - 1

        while srow <= erow and scol <= ecol:
            # 1️⃣ Traverse the top row (left → right)
            for j in range(scol, ecol + 1): # ecol +1 to include ecol, range is exclusive of end
                result.append(mat[srow][j])
            srow += 1

            # 2️⃣ Traverse the right column (top → bottom)
            for i in range(srow, erow + 1): # erow +1 to include erow
                result.append(mat[i][ecol])
            ecol -= 1

            # 3️⃣ Traverse the bottom row (right → left)
            if srow <= erow:
                for j in range(ecol, scol - 1, -1): # -1 for reverse, scol -1 to include scol
                    result.append(mat[erow][j])
                erow -= 1

            # 4️⃣ Traverse the left column (bottom → top)
            if scol <= ecol:
                for i in range(erow, srow - 1, -1):
                    result.append(mat[i][scol])
                scol += 1

        return result
#example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
solution = Solution()

print(solution.spiralOrder(matrix))
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

'''---------------------------------------------------'''
'''2)Given a square matrix mat[][] of size n x n. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.'''

def rotateMatrix(mat):
    n = len(mat)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n): # j=i to avoid double swapping
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # Reverse each column
    for j in range(n):
        for i in range(n // 2): # only half rows tak jana h
            mat[i][j], mat[n - 1 - i][j] = mat[n - 1 - i][j], mat[i][j]
    
    return mat

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated_matrix = rotateMatrix(matrix)
for row in rotated_matrix:
    print(row)
# Output:
# [3, 6, 9] 
# [2, 5, 8]
# [1, 4, 7]
'''-----------------------or----------------------------'''

#clockwise

def rotateMatrixClockwise(mat):
    n = len(mat)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n): # j=i to avoid double swapping
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # Reverse each row
    for i in range(n):
        for j in range(n // 2): # only half columns tak jana h
            mat[i][j], mat[i][n - 1 - j] = mat[i][n - 1 - j], mat[i][j]
    
    return mat
# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated_matrix = rotateMatrixClockwise(matrix)
for row in rotated_matrix:
    print(row)
# Output:
# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3] 
'''---------------------------------------------------'''

'''3)Given a 2D integer matrix mat[][] of size n x m, where every row and column is sorted in increasing order and a number x, 
the task is to find whether element x is present in the matrix.'''

#note the properties of the matrix:
'''->Each row is sorted in ascending order.
   ->The first element of each row is greater than or equal to the last element of the previous row.'''

class Solution:
    def searchMatrix(self, mat, x): # mat is 2D matrix, x is target element
        if not mat:
            return False

        n = len(mat)      # number of rows
        m = len(mat[0])   # number of columns

        row, col = 0, m - 1  # Start from the top-right corner, m -1 for last column index

        while row < n and col >= 0: # row ko increment karna h down me jane keliye and col ko decrement karna h left me jane ke liye
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False
# Example usage:
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
solution = Solution()
print(solution.searchMatrix(matrix, 9))   # Output: True
print(solution.searchMatrix(matrix, 4))   # Output: False

'''---------------------------------------------------------------------'''
'''4)Given a row-wise sorted 2D matrix mat[][] of size n x m and an integer x, find whether element x is present in the matrix.
Note: In a row-wise sorted matrix, each row is sorted in itself, i.e. for any i, j within bounds, mat[i][j] <= mat[i][j+1].'''

class Solution:
    def searchMatrix(self, mat, x):
        if not mat:
            return False

        n = len(mat)      # number of rows
        m = len(mat[0])   # number of columns

        for i in range(n):
            # Perform binary search on each row
            left, right = 0, m - 1
            while left <= right:
                mid = left + (right - left) // 2 # to avoid overflow 0+(2-0)//2=1
                if mat[i][mid] == x: # mid = middle element of the current row, mat[0][1] for first row
                    return True
                elif mat[i][mid] < x: #If the middle element is smaller than the target, search in the right half
                    left = mid + 1
                else:
                    right = mid - 1 #If the middle element is larger than the target, search in the left half
#now 1st row nothing match second row search initialize hoga left=0,right=m-1
        return False
# Example usage:
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]   
solution = Solution()
print(solution.searchMatrix(matrix, 9))   # Output: True
print(solution.searchMatrix(matrix, 4))   # Output: False

'''-----------------------------------------------------------'''

'''5)Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.'''

class Solution:
    def searchMatrix(self, mat, x):
        if not mat:
            return False

        n = len(mat)      # number of rows
        m = len(mat[0])   # number of columns

        left, right = 0, n * m - 1  # Treat the matrix as a 1D array

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = mat[mid // m][mid % m]  # Convert 1D index to 2D indices

            if mid_value == x:
                return True
            elif mid_value < x:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
# Example usage:
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
solution = Solution()
print(solution.searchMatrix(matrix, 9))   # Output: True
print(solution.searchMatrix(matrix, 4))   # Output: False

'''-----------------------------------------------------------'''
class Solution:
    # --- Binary Search 1: Find target row --- target row dhundna h first baad me us row me search karna h target element
    def findRow(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        startRow, endRow = 0, n - 1

        while startRow <= endRow:
            midRow = startRow + (endRow - startRow) // 2

            # Check if x lies within this row's range
            if mat[midRow][0] <= x <= mat[midRow][m - 1]: # m-1 for last element of the row (m columns last col))
                return midRow
            elif x < mat[midRow][0]: # x is smaller than the first element of midRow
                endRow = midRow - 1
            else:
                startRow = midRow + 1

        return -1  # No suitable row found

    # --- Binary Search 2: Search inside the found row ---
    def binarySearchRow(self, row, x):
        startCol, endCol = 0, len(row) - 1

        while startCol <= endCol:
            midCol = startCol + (endCol - startCol) // 2 # midCol is the middle index of the current row
            if row[midCol] == x:
                return True
            elif row[midCol] < x:
                startCol = midCol + 1
            else:
                endCol = midCol - 1
        return False

    # --- Main Function ---
    def searchMatrix(self, mat, x):
        if not mat:
            return False

        # Step 1: Find which row may contain x
        ##Jab fun call kar rahe h to self lagana nahi h
        target_row = self.findRow(mat, x)
        if target_row == -1:
            return False

        # Step 2: Search inside that row
        ##We are not using self here because binarySearchRow is being called from within the same class context.
        return self.binarySearchRow(mat[target_row], x)
    
# Example usage:
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
solution = Solution()
print(solution.searchMatrix(matrix, 9))   # Output: True
print(solution.searchMatrix(matrix, 4))   # Output: False

'''----------------------------------------------------------- '''

'''6)You are given a 2D matrix mat[][] of size n x m. The task is to modify the matrix such that if mat[i][j] is 0, 
all the elements in the i-th row and j-th column are set to 0.'''

def setZeroes(mat):
    if not mat:
        return

    n = len(mat)      # number of rows
    m = len(mat[0])   # number of columns

    # Create two sets to keep track of rows and columns to be zeroed
    rows_to_zero = set() #tracking kar rahe h rows ke liye.--> empty set aise define karte h
    cols_to_zero = set() #tracking kar rahe h columns ke liye.

    # First pass: identify all rows and columns that need to be zeroed
    #jo bhi 0 h uske row and column ko store karna h upar ke sets me.
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)

    # Second pass: set the identified rows and columns to zero
    for i in range(n):
        for j in range(m):
            if i in rows_to_zero or j in cols_to_zero:
                mat[i][j] = 0

# Example usage:
matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [0, 8, 9]
]
setZeroes(matrix)
for row in matrix:
    print(row)  
# Output:
# [0, 0, 0]
'''------------------------------or-----------------------------'''

def setZeroes(mat):
    if not mat:
        return

    n = len(mat)      # number of rows
    m = len(mat[0])   # number of columns

    row_zero = False  # Flag to indicate if the first row needs to be zeroed
    col_zero = False  # Flag to indicate if the first column needs to be zeroed

    # First pass: use first row and first column as markers
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                if i == 0:
                    row_zero = True
                if j == 0:
                    col_zero = True
                mat[i][0] = 0  # Mark the first cell of the row
                mat[0][j] = 0  # Mark the first cell of the column

    # Second pass: set zeros based on markers
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0

    # Finally, zero out the first row and first column if needed
    if row_zero:
        for j in range(m):
            mat[0][j] = 0

    if col_zero:
        for i in range(n):
            mat[i][0] = 0
# Example usage:
matrix = [
    [1, 2, 0],
    [4, 5, 6],
    [0, 8, 9]
]
setZeroes(matrix)
for row in matrix:
    print(row)  
# Output:
# [0, 0, 0] 
