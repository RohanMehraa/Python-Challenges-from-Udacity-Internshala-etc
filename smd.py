# WAP TO ACCEPT A NO. AND FIND THE SUM OF DIGITS OF THAT NO. :
tmp = num = int(input("Please enter a no. : "))
sm = 0

while num>0:
    dig = num % 10
    sm +=  dig
    num //= 10

print("\nSUM OF DIGITS OF {} = ".format(tmp), sm)