num = int(input("Please enter the no. you want to check : "))
flag = 0

for i in range(2, (num//2)+1):
    if num % i == 0:
       flag = 1
       break

if flag == 0:
    print(num, " is a Prime no.")

else:
    print(num, " is a Composite no.")