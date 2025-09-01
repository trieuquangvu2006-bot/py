# 1. Write a Python program to sum all the items in a list
numbers  = [1, 2, 3 , 5, 6]
tong = 0
for i in numbers:
    tong += i
print("Tổng các phần tử là: ", tong)

# 2. Write a Python program to multiply all the items in a list.
numbers= [1, 2, 3, 4, 5]
tich = 1
for x in numbers:
    tich *= x
print("Tích các phần tử trong list là: ", tich)

# 3. Write a Python program to get the largest number from a list
a = [ 5, 7, 6, 12, 54, 76]
print("Số lớn nhất là:",max(a))

# 4. Write a Python program to get the smallest number from a list.
a = [2, 6, 8, 4, 24, 17, 30]
print("Số nhỏ nhất là : ", min(a))

# 5. Write a Python program to count the number of strings from a given list of
# strings. The string length is 2 or more and the first and last characters are the
# same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
words = ["abc", "xyz", "aba", "1221"]
count = 0
for w in words:
    if w in words:
        if len(w) >= 2 and w[0] == w[-1]:
            count += 1
print("Kết quả:", count)

# 6. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last_element(t):
    return t[-1]
list_tuples = [(2,5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sorted(list_tuples, key=last_element)
print(result)

# 7. Write a  Python program to remove duplicates from a list.
numbers = [1, 2, 3, 3, 4, 4, 5]
unique_list = []
for x in numbers:
    if x not in unique_list:
        unique_list.append(x)
print("List sau khi xóa trùng: ", unique_list)

# 8. Write a  Python program to check if a list is empty or not.
a =[]
if len(a) == 0:
     print("List rỗng")
else:
     print("List không rỗng")

# 9. Write a Python program to clone or copy a list.
a = ["Quoc khanh 2/9", 2, 9, 1, 9, 4, 5 ]
b = a.copy()
print("List gốc: ", a)
print("List copy: ", b)

# 10. Write a Python program to find the list of words that are longer than n from a
# given list of words.

words = ["Python", "is", "beautiful", "language"]
print("Nhập vào n:")
n = int(input())
result = []
for w in words:
    if len(w) > n:
        result.append(w)
print("Các từ có độ dài lớn hơn ", n , "là :", result)

# 11. Write a Python function that takes two lists and returns True if they have at
# least one common member.
a = [1, 2, 3, 4, 5]
b = [2, 4, 7, 8, 9]
found = False
for i in a:
    if i in b:
        print("true(phần tử chung là: ", i, ") ")
        found = True
        break
if not found:
    print("false(không phần tử chung) ")

# 12. Write a Python program to print a specified list after removing the 0th, 4th
# and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

a = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
a.pop(5)
a.pop(4)
a.pop(0)
print(a)

# 13. Write a  Python program to generate a 3*4*6 3D array whose each element is
# *.

# 14. Write a  Python program to print the numbers of a specified list after removing
# even numbers from it.
numbers = [1, 2, 3, 5, 6, 7, 8, 9 , 10]
result = []
for num in numbers:
    if num % 2 != 0:
        result.append(num)
print("Danh sách các số sau khi loại bỏ số chẵn là: ", result)
# 15. Write a Python program to shuffle and print a specified list. {shuffle: xáo trộn ngẫu nhiên}

# 16. Write a Python program to generate and print a list of the first and last 5
# elements where the values are square numbers between 1 and 30 (both included).
squares = [x**2 for x in range(1, 31)]
print("5 phần tử đầu: ", squares[:5])
print("5 phần tử cuối: ", squares[-5:])

# 17. Write a Python program to check if each number is prime in a given list of
# numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def all_primes(lst):
    for num in lst:
        if not is_prime(num):
            return False
    return True
print(all_primes([0, 3, 4, 7, 9]))
print(all_primes([3, 5, 7, 13]))
print(all_primes([1, 5, 3]))
# 18. Write a  Python program to generate all permutations of a list in  Python.

# 19. Write a Python program to calculate the difference between the two lists.

# 20. Write a Python program to access the index of a list.
colors = ["red", "green", "blue"]
for i in range(len(colors)):
    print("Index:", i, "Value:", colors[i])

# 21. Write a Python program to convert a list of characters into a string.
chars = ["H", "e", "l", "l", "o"]
result= ""
for c in chars:
    result += c
print(result)

# 22. Write a Python program to find the index of an item in a specified list.
colors = ["red", "green", "blue", "green"]
print(colors.index("green"))
print(colors.index("blue"))

# 23. Write a Python program to flatten a shallow list.

# 24. Write a Python program to append a list to the second list.
a = [1, 2, 3]
b = [4, 5]
b.extend(a)
print(b)

# 25. Write a Python program to select an item randomly from a list.

# 26. Write a  Python program to check whether two lists are circularly identical.  ***
def circularly_identical(a, b):
    if len(a) != len(b):
        return False
    double_a = a * 2
    return str(b)[1:-1] in str (double_a)[1:-1]
A= [10, 10, 0, 0, 10]
B = [10, 0, 0, 10, 10]
print(circularly_identical(A, B))

# 27. Write a  Python program to find the second smallest number in a list.  ***
def second_smallest(nums):
    uniq = sorted(set(nums))
    if len(uniq) < 2:
        raise ValueError("Không tồn tại số nhỏ thứ hai")
    return uniq[1]
print(second_smallest([1, 2, 3, 4]))
print(second_smallest([1, 1, 1, 2]))

# 28. Write a Python program to find the second largest number in a list.  ***
def second_largest(nums):
    uniq = sorted(set(nums), reverse=True)
    if len(uniq) < 2:
        raise ValueError("Không tồn tại số lớn thứ hai")
    return uniq[1]
print(second_largest([1, 2, 3, 4]))
print(second_largest([10, 10, 9, 8]))

# 29. Write a Python program to get unique values from a list.  ***
nums = [1, 2, 3, 1, 2, 4, 5]
unique_vals = list(set(nums))
print(unique_vals)

# 30. Write a Python program to get the frequency of elements in a list. ***
nums = [1, 2, 3, 4, 4, 4, 5]
freq = {}
for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(freq)

# 31. Write a Python program to count the number of elements in a list within a
# specified range.
def count_in_range(nums, low, high):
    count = 0
    for x in nums:
        if low <= x <= high:
            count += 1
    return count
nums = [10, 20, 30, 40, 50]
print(count_in_range(nums, 15, 45))

# 32. Write a Python program to check whether a list contains a sublist.
def contains_sublist(lst,sub):
    return str(sub)[1:-1] in str(lst)[1:-1]
print(contains_sublist([1, 2, 3, 4, 5], [2, 3]))
print(contains_sublist([1, 2, 3, 4, 5], [2, 4]))

# 33. Write a  Python program to generate all sublists of a list.
def all_sublists(lst):
    result = [[]]
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(lst[i:j])
    return result
nums = [1, 2, 3]
print(all_sublists(nums))

# 34. Write a  Python program that uses the Sieve of Eratosthenes method to
# compute prime numbers up to a specified number.
# Note: In  mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον
# Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number
# sieves, is a simple, ancient algorithm for finding all prime numbers up to any
# given limit.

# 35. Write a Python program to create a list by concatenating a given list with a
# range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# 36. Write a  Python program to get a variable with an identification number or
# string.
x = 100
print("Value", x)
print("ID:", id(x))
# 37. Write a  Python program to find common items in two lists.
a = [1, 2, 3, 4, 5]
b = [2, 4 ,5 ,6 ,3]
common = list(set(a) & set(b))
print(common)

# 38. Write a Python program to change the position of every n-th value to the
# (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def swap_pairs(lst):
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
nums = [0, 1, 2, 3, 4, 5]
print(swap_pairs(nums))

# 39. Write a Python program to convert a list of multiple integers into a single
# integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
nums = [11, 33, 50]
result_str = ""
for n in nums:
    result_str += str(n)
result = int(result_str)
print(result)

# 40. Write a Python program to split a list based on the first character of a word.
def split_by_first_char(words):
    result = {}
    for word in words:
        key = word[0]
        if key not in result:
            result[key] = []
        result[key].append(word)
    return result
words = ["apple", "banana", "apricot", "chery", "blueberry"]
print(split_by_first_char(words))

# 41. Write a  Python program to create multiple lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

# 43. Write a  Python program to split a list into different variables.
colors = ["Red", "Green", "Blue"]
c1, c2, c3 = colors
print(c1)
print(c2)
print(c3)
# 44. Write a Python program to generate groups of five consecutive numbers in a
# list.
# 45. Write a Python program to convert a pair of values into a sorted unique array.
pairs = [(1, 2), (3, 4), (1, 2)]
result = sorted(set(sum(pairs, ())))
print(result)

# 46. Write a Python program to select the odd items from a list.
nums = [10, 20, 30, 40, 50, 60]
odd_items = nums[1::2]
print(odd_items)

# 47. Write a Python program to insert an element before each element of a list.
def insert_before_each(lst, elem):
    result = []
    for x in lst:
        result.append(elem)
        result.append(x)
    return result
nums = [1, 2, 3, 4]
print(insert_before_each(nums, "X"))

# 48. Write a  Python program to print nested lists (each list on a new line) using
# the print() function.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in nested_list:
    print(sublist)

# 53. Write a Python program to create a list with infinite elements.

# 54. Write a  Python program to concatenate elements of a list.
items = ["A", "B", "C"]
result =""
for item in items:
    result += str(item)
print(result)
# 55. Write a Python program to remove key-value pairs from a list of dictionaries.
data = [
    {"id": 1, "name":"Ahihi", "age": 25},
    {"id": 2, "name":"aheee", "age": 30},
    {"id": 3, "name":"ahoho", "age": 34},
]
for d in data:
    d.pop("age", None)
print(data)
# 56. Write a Python program to convert a string to a list.
s = "Python"
char_list = list(s)
print(char_list)

# 57. Write a Python program to check if all items in a given list of strings are equal
# to a given string.
words = ["yes", "yes", "yes"]
print(set(words) == {"yes"})
print(set(words) == {"no"})

# 58. Write a  Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8 ]
result = list1[:-1] + list2
print(result)

# 59. Write a  Python program to check whether the n-th element exists in a given
# list.
def check_nth_element(lst, n):
    if 0 <= n < len(lst):
        return True
    return False
data = [10, 20, 30, 40]
print(check_nth_element(data, 2))
print(check_nth_element(data, 5))

# 60. Write a Python program to find a tuple, the smallest second index value from
# a list of tuples.
data = [(1, 5), (2, 2), (3, 8), (4, 1)]
result = min(data, key=lambda x: x[1])
print(result)

# 78. Write a  Python program to split a given list into two parts where the length of
# the first part of the list is given.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splited the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])

def split_list(lst, n):
    return (lst[:n], lst[n:])
orginal_list = [1, 1, 2, 3, 4, 4, 5, 1]
n = 3
result = split_list(orginal_list, n)
print("Orginal list:", orginal_list)
print("Length of the firts part of the list:", n)
print("Splited the said list into two parts:", result)
# 79. Write a Python program to remove the K'th element from a given list, and
# print the updated list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]
lst = [1, 1, 2, 3, 4, 4, 5, 1]
k = 2
del lst[k]
print(lst)

# 80. Write a  Python program to insert an element at a specified position into a
# given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]

lst = [1, 1, 2, 3, 4, 4, 5, 1]
k = 2
elem = 12
lst.insert(k, elem)
print(lst)

# 81. Write a  Python program to extract a given number of randomly selected
# elements from a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]
import random
lst = [1, 1, 2, 3, 4, 4, 5, 1]
k = 3
result = random.sample(lst, k)
print(result)

# 191. Write a  Python program to find the maximum and minimum values of the
# three given lists.
# Original lists:
# [2, 3, 5, 8, 7, 2, 3]
# [4, 3, 9, 0, 4, 3, 9]
# [2, 1, 5, 6, 5, 5, 4]
# Maximum value of the said three lists:
# 9
# Minimum value of the said three lists:
# 0
list1 = [2, 3, 5, 8, 7, 2, 3]
list2 = [4, 3, 9, 0, 4, 3, 9]
list3 = [2, 1, 5, 6, 5, 5, 4]
max_val = max(max(list1), max(list2), max(list3))
min_val = min(min(list1), min(list2), min(list3))
print("Maximum value of the said three lists:", max_val)
print("Minimum value of the said three lists:", min_val)

# 223. Write a  Python program to create a list with non-unique values filtered out.
nums = [1, 2, 3, 2, 4, 5, 1, 3]
non_unique = list(set([x for x in nums if nums.count(x) > 1]))
print(non_unique)
# 224. Write a Python program to create a list with unique values filtered out.
nums = [1, 2, 3, 2, 4, 5, 1, 3]
unique_only = [x for x in nums if nums.count(x) == 1]
print(unique_only)

# 259. Write a  Python program to check if a given function returns True for at least
# one element in the list.
# Sample Output:
# False
# True
# False
def check_any(lst, func):
    return any(func(x) for x in lst)
nums = [1, 3, 5]
print(check_any(nums, lambda x: x % 2 == 0))
nums = [1, 4, 7]
print(check_any(nums, lambda x: x % 2 == 0))
nums = []
print(check_any(nums, lambda x: x > 0))

# 260. Write a Python program to check if all the elements of a list are included in
# another given list.
# Sample Output:
# True
# False
def is_included (list1, list2):
    return set(list1).issubset(list2)
print(is_included([1, 2, 3], [1, 2, 3, 4, 5]))
print(is_included([1, 6], [1, 2, 3, 4, 5]))