def reverse_string(text):
    return text[::-1]


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

def is_prime(num):
    flag = False
    if num == 0 or num == 1:
        print(f'{num} is not a prime number')
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f'{num} is a prime number')
                flag = True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
    return