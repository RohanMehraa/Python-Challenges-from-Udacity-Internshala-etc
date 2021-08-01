i = 0
print("\nPlease enter 5 no.(s)...")

while i<5:
    num = int(input())
    if i==0:
        gr = sm = num
    elif num > gr:
        gr = num
    elif num < sm:
        sm = num
    i += 1
    
print("Greatest no. is :", gr)
print("Smallest no. is :", sm)
