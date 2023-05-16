#You are given a two-dimesnional array (a matrix) of potentially unequal height and width,
#containing only 0 s and 1 s. Each 0 represents land, and each 1 represent part of the river.
#A river consist of any number of 1 s that are either horizontally or vertically adjacent 
#(but not diagonally adjacent). The number of adjacent 1 s forming a river determine its size. 
#Note that a river can twist. In other words. It doesn't have to be a straight vertically line 
#or a straight horizontal line; it can be L-shaped, for example
#Write a function called riverSizes with attribute matrix that returns an array of the sizes 
#of all rivers represented in the input matrix. The sizes don't need to be in any particular order.


def riverSizes(matrix): #otro comment2
    sizes = []  # create an empty list to store sizes of rivers
    for i in range(len(matrix)):  # iterate over rows of matrix
        for j in range(len(matrix[i])):  # iterate over columns of matrix
            if matrix[i][j] == 1:  # if cell contains a 1, start counting river size
                size = getRiverSize(matrix, i, j)  # get size of river starting at current cellllll
                sizes.append(size)  # add size of river to list of river sizes
    return sizes  # return list of river sizes

def getRiverSize(matrix, i, j):
    # recursive function to get the size of the river starting at cell i, j
    # if cell is out of bounds or not part of a river, return 0
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != 1:
        return 0
    matrix[i][j] = 0  # mark cell as visited
    size = 1  # initialize size of river to 1
    # recursively call getRiverSize on all adjacent cells that are part of the same river
    size += getRiverSize(matrix, i + 1, j)  # down
    size += getRiverSize(matrix, i - 1, j)  # up
    size += getRiverSize(matrix, i, j + 1)  # right
    size += getRiverSize(matrix, i, j - 1)  # left
    return size  # return size of river

# Input matrix
matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

# Compute river sizes
river_sizes = riverSizes(matrix)

# Print river sizes
print("River sizes:", river_sizes)

#The output indicates that there are 5 rivers, with sizes 2, 1, 5, 2, and 2, respectively, as previously explained.

#Explanation
#The function riverSizes takes in the matrix as an argument and returns an array of the sizes of all the rivers 
#in the matrix. It first initializes an empty array called sizes that will hold the sizes of all the rivers. 
#Then it loops over every cell in the matrix using two nested for loops. If a cell contains a 1, 
#it means that it is the beginning of a river. We then call the getRiverSize function to determine the size of the river
#and add it to the sizes array. Finally, we return the sizes array.
#The function getRiverSize takes in the matrix, the indices of the current cell (i and j),
#and returns the size of the river starting at the current cell. We first check whether the current cell is out of bounds
#or not a part of a river (i.e., the cell contains a 0). If so, we return 0.
#Otherwise, we mark the current cell as visited by setting it to 0, and initialize the size of the river to 1. 
#We then recursively call getRiverSize on each adjacent cell (up, down, left, and right) 
#that is also part of the river, and add the size of each sub-river to the size variable.
#Finally, we return the size of the river.