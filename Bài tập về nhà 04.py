# 1.Write a Python function to find the maximum of three numbers.
def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b>= a and b >= c:
        return b
    else:
        return c
print(maximum_of_three(10, 25, 7))

# 2.Write a Python function to sum all the numbers in a list.
def sum_in_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_in_list([1,2,3,4,5,6,7]))

# 3.Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))
print(factorial(0))
# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    #Kiểm tra đến căn bậc hai của n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
print(is_prime(2))
print(is_prime(17))
print(is_prime(20))

# 6.Write a Python function to print
# 1.all prime numbers that less than a number (enter prompt keyboard).
# 2.the first N prime numbers
def primes_less_than_n():
    n = int(input("Nhập một số: "))
    primes = []
    for num in range(2, n): # Kiểm tra từ 2 đến n - 1
        if is_prime(num):  # dùng hàm is_prime đã viết ở bài 5
            primes.append(num)
    print(f"Các số nguyên tố nhỏ hơn {n} là: ", primes)

# Hàm kiểm tra số nguyên tố (dùng lại từ bài 5)
def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

# In N số nguyên tố đầu tiên
def first_n_primes(N):
    primes = []
    num = 2
    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1
    print(f"{N} số nguyên tố đầu tiên là:", primes)

if __name__ == "__main__":
    primes_less_than_n()
    first_n_primes(100)

# 7.Write a Python function to check whether a number is "Perfect" or not. Then print all perfect number that less than 1000.

# Hàm kiểm tra Perfect number
def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = 1 # luôn có ước là 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n
# In tất cả các số perfect number nhỏ hơn 1000
def perfect_numbers_below_1000():
    perfects = []
    for num in range(2, 1000):
        if is_perfect(num):
            perfects.append(num)
    print("Các số perfect numbers nhỏ hơn 1000 là: ", perfects)
if __name__ == "__main__":
 perfect_numbers_below_1000()

# 8.Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog
import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase) # tập hợp 26 chữ cái thường
    return alphabet.issubset(set(s.lower()))
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello world"))