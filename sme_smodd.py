#WAP TO ACCEPT 5 NO.S FROM USER AND PRINT SUM OF EVEN AND ODD NO.S
i = sme = smo = 0
print("\nPLEASE ENTER FIVE NO.(S) :")
while i<5:
    num = int(input())
    if num%2 == 0:
        sme += num
    else:
        smo += num
    i += 1

print("\nSUM OF EVEN INPUTS = ", sme)
print("\nSUM OF ODD INPUTS = ", smo)
