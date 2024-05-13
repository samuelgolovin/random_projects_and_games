cols = 8  # Example value for the number of columns in the board
pos = 15  # Example value for the position in the 1D array representing the board

# Calculate the row and column indices of the cell at position `pos`
row = pos // cols  # Integer division to get the row index
col = pos % cols   # Modulo operation to get the column index

print("Row:", row)  # Output: Row: 1
print("Column:", col)  # Output: Column: 7
