def prime_occur(limit):
    count, flag = 0, 0
    for num in range(2, limit+1):
        for i in range(2, num//2+1):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            count += 1
        else:
            flag = 0
    return count
    

def main():
    limit = int(input("\nINPUT THE LIMIT TILL YOU WANT TO COUNT THE PRIME NO. OCCURANCE  :  "))
    print("\nTOTAL PRIME NO.(S) OCCURRED TILL {} IS  : ".format(limit), prime_occur(limit))


main()