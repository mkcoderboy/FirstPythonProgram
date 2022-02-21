

# 2D list means, lists within a list.

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10]
]

# Lists within the list is also indexed.

print(number_grid[0])

# Can print out a specific number from row and colum.

print(number_grid[2][1])


# ---------------------------------------------------------------------------------------------------------

# Nested forloop is a for loop within a for loop.
# This will print out all the numbers in the grid.
for row in number_grid:
    for col in row:
        print(col)

