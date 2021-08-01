print("\n\nEnter the size of matrix....")
row = int(input("Row:\t"))
col = int(input("Column:\t"))

matrix = list()
even_row = list()
odd_row = list()

for i in range(2):
    for j in range(col):
        if i % 2 == 0:
            if j % 2 == 0:
                even_row.append(1)

            else:
                even_row.append(0)

        else:
            if j % 2 == 1:
                odd_row.append(1)

            else:
                odd_row.append(0)            

for i in range(row):
    if i % 2 == 0:
        matrix.append(even_row)
    else:
        matrix.append(odd_row)

print("\n\nAFTER OPERATIONS MATRIX IS... \n")
for i in range(row):
    print(matrix[i])
    