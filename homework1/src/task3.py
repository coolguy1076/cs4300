def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def first_10_primes():
    primes = []
    num = 2
    while len(primes) < 10:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def sum_1_to_100():
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total

