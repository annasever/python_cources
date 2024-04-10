def is_prime(number: int) -> bool:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input('Enter number for checking from 2 to 1000: '))
if 2 <= number <= 1000:
    if is_prime(number):
        print(f'{number} is prime')
    else:
        print(f'{number} is not prime')
else:
    print('This number does not belong to the necessary interval of numbers')
