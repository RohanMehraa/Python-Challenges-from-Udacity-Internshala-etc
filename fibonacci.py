# PRINT FIBONACCI SERIES TILL DESIRED USER INPUT:
a, b = 0, 1
limit=int(input("\nPLEASE ENTER THE LIMIT TILL YOU WANT TO PRINT THE SERIES:"))
print("FIBONACCI SERIES TILL {}....".format(limit))
while a <= limit:
    print(a, end=' ')
    c = a+b
    a = b
    b = c
