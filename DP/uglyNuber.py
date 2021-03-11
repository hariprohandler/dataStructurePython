def is_ugly(num, divisor):
    print(f"Divisor is {divisor}")
    if(divisor <= 1 ):
        return True
    if(
        (num % divisor == 0
        and divisor not in [2,3,5])
        or
        (divisor in [2,3,4] and num % divisor != 0)
    ):
        return False
    return is_ugly(num, divisor-1);

number = int(input("Enter Number of ugly numbers to be printed "))
print(number);
print(is_ugly(number, (number// 2)))