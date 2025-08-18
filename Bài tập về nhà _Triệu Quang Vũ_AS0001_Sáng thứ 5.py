# 1. Write a Python program to calculate the length of a string.
s = "Hello World"
print("Độ dài chuỗi: ", len(s))

# 2. Write a Python program to count the number of characters (character frequency) in a string.
from collections import Counter

s = "hom nay troi dep qua di thoiiii"
freq = Counter(s)
print(freq)

# 9. Write a Python program to remove the nth index character from a nonempty string.
s = "Hoc python thoi nao"
n = 4
result = s[:n] + s[n + 1:]
print("Chuỗi gốc:", s)
print(f"Chuỗi sau khi xóa ký tự tại index {n}:", result)

# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
s = "ThanThiDet"
new_s = s[-1] + s[1:-1] + s[0]
print(new_s)

# 11.Write a Python program to remove characters that have odd index values in a given string.
s = "Xinchao"
new_s = s[::2]
print(new_s)

# 12. Write a Python program to count the occurrences of each word in a given sentence.
s = " mot ngay di hoc la mot ngay vui"
words = s.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 13. Write a  Python  script that takes input from the user and displays that input back in upper and lower cases
s = input(" Nhập chuỗi: ")
print("In hoa:", s.upper())
print("In thường: ", s.lower())

# 14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
s = "red, white, black, green"
words = [w.strip() for w in s.split(",")]
words.sort()
print(",".join(words))

#18.Write a  Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
s = "Hoc Python tu dau cho Tit"
if len(s) < 3:
    print(s)
else:
    print(s[:3])

#19. Write a Python program to get the last part of a string before a specified character.
s = "https://www.w3resource.com/python-excercises"
print(s.split("/")[2])

#24.Write a Python program to check whether a string starts with specified characters.
s = "python exercises"
print(s.startswith("py"))
print(s.startswith("c++"))

#3 Write a  Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
s = "w3resource"
if len(s) < 2:
    print("")
else:
    print(s[:2] + s[-2:])

#4 Write a  Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
s = "restart"
first = s[0]
new_s = first + s[1:].replace(first, "$")
print(new_s)

#5.Write a  Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a, b = "abc", "xyz"
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print(new_a + " " + new_b)

#6 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
s = "string"
if len(s) < 3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")

#16 Write a Python function to insert a string in the middle of a string.
def insert_middle(wrapper, word):
    mid = len(wrapper) // 2
    return wrapper[:mid] + word + wrapper[mid:]
print(insert_middle("{{}}", "PHP"))
print(insert_middle("[[]]<<>>", "Python"))

#17.Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
s = "python"
print(s[-2:] * 4)

#20 Write a  Python function to reverse a string if its length is a multiple of 4.
s = "abcd"
if len(s) % 4 == 0:
    print(s[::-1])
else:
    print(s)
#22 Write a  Python program to sort a string lexicographically.
s = "Hello World"
print("".join(sorted(s)))

#28 Write a Python program to add prefix text to all of the lines in a string.
text = "Xinchao\nHello\nAnhonxeo"
prefixed = "\n".join("->" + line for line in text.split("\n"))
print(prefixed)

#39. Write a  Python program to reverse a string.
s = "Pythonnnnnnnnn"
print(s[::-1])

#40.Write a Python program to reverse words in a string.
s = "Hom nay troi dep qua di thoi"
words = s.split()
print(" ".join(words[::-1]))

#41  Write a  Python program to strip a set of characters from a string.
s = "Than Thi Det"
chars_to_remove = "ait"
result = "".join(c for c in s if c not in chars_to_remove)
print(result)

#42 Write a Python program to count repeated characters in a string.
s = " thequickbrownfoxjumpsoverthelazydog"
freg = {}
for c in s:
    freg[c] = freg.get(c, 0) + 1
for k, v in freg.items():
    if v > 1:
        print(k, v)

#44 Write a  Python program to print the index of a character in a string.
s = "w3resource"
for i, c in enumerate(s):
    print(f"ký tự {c} ở vị trí {i}")

#46. Write a Python program to convert a given string into a list of words.
s = "The quick brown for jumps"
words  = s.split()
print(words)

#49. Write a Python program to count and display vowels in text.
S = "Xin chao Anh Ti Anh Teo"
vowels = "ueoaiUEOAI"
count = 0
for c in S:
    if c in vowels:
        count += 1
print("Số nguyên âm:", count)

#51. Write a  Python program to find the first non-repeating character in a given string.
s = "abccbde"
for c in s:
    if s.count (c) == 1:
        print("Ký tự không lặp lại đầu tiên:", c)
        break

#53. Write a Python program to find the first repeated character in a given string.
s = "abcdea"
seen = set()
for c in s:
    if c in seen:
        print("Ký tự lặp lại đầu tiên:", c)
        break
    seen.add(c)

#55.Write a Python program to find the first repeated word in a given string.
s = (" Day la bai tap ve nha cho cac ban hoc lop buoi sang lap trinh co ban")
words  = s.lower().split()
seen = set()
for w in words:
    if w in seen:
        print(" Từ lặp lại đầu tiên:", w)
        break
    seen.add(w)

#57.Write a  Python program to remove spaces from a given string.
s = "Hello   world   "
print(s.strip())
print(s.replace(" ", " "))

# 60. Write a  Python program to capitalize the first and last letters of each word in a given string.
s = "python exercises"
result = " ".join(word[0].upper() + word[1:-1] + word[-1].upper() for word in s.split())
print(result)

#61. Write a Python program to remove duplicate characters from a given string.
s = "aabbccdddeeff"
result = "".join(dict.fromkeys(s))
print(result)

#62. Write a Python program to compute the sum of the digits in a given string.
s ="abcxyz123567"
total = sum(int(c) for c in s if c.isdigit())
print(total)

#63. Write a Python program to remove leading zeros from an IP address.
ip ="192.168.001.001"
parts = ip.split(".")
clean = ".".join(str(int(p)) for p in parts)
print(clean)

#67. Write a Python program to remove all consecutive duplicates of a given string.
s = "aabbbaaaccd"
result = s[0]
for c in s[1:]:
    if c != result[-1]:
        result += c
print(result)

#70. Write a  Python program that concatenates uncommon characters from two strings.
a, b = "abcd", "bcdf"
result = "".join(sorted(set(a) ^ set(b)))
print(result)

#72. Write a Python program to remove all characters except a specified character from a given string...
s = "google"
keep = "g"
result = "".join(c for c in s if c == keep)
print(result)

#73. Write a  Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
s = "Hello123!!!"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
digit = sum(1 for c in s if c.isdigit())
special = len(s) - (upper + lower + digit)
print("Chữ hoa:", upper)
print("Chữ thường:", lower)
print("Số:", digit)
print("Ký tự đặc biệt:", special)

#79. Write a Python program to find the smallest and largest words in a given string.
s = " The quick brown fox jumps over the lazy dog"
words = s.split()
print("Ngắn nhất:", min(words, key=len))
print("Dài nhất:", max(words, key = len))

#84. Write a Python program to swap cases in a given string.
s = "Python EXERCISES"
print(s.swapcase())

#86. Write a  Python program to delete all occurrences of a specified character in a given string.
s = "Delete all occurrences of a specified character"
ch = "e"
result = s.replace(ch, "")
print(result)

#87. Write a  Python program to find the common values that appear in two given strings.
a, b = "Python3","Python2.7"
common = "".join(sorted(set(a) & set(b)))
print(common)

#88. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
s = "W3bresource"
ok = (any(c.isupper()for c in s) and
      any(c.islower() for c in s) and
      any(c.isdigit() for c in s) and
      len(s) >= 8)
print("Valid string" if ok else "Invalid string")

#89.Write a  Python program to remove unwanted characters from a given string.
import re
s = "Pyth*^on Exercis^es"
clean = re.sub(r"[^a-zA-Z0-9 ]", "", s)
print(clean)

#90. Write a Python program to remove duplicate words from a given string.
s = "Python Exercises Practice Solution Excercises"
words = s.split()
result = " ".join(dict.fromkeys(words))
print(result)

#93.  Write a Python program to extract numbers from a given string.
import re
s = "red 12 black 45 green"
nums = re.findall(r"\d+", s)
print([int(n) for n in nums])

#96 Write a  Python program to convert a given string to Camelcase.
s = "python excercises"
words = s.split()
camel = words[0].lower() + "".join(w.capitalize() for w in words[1:])
print(camel)

#97 Write a Python program to convert a given string to Snake case.
s = "Python Exercises Practice"
snake = "_".join(s.lower().split())
print(snake)

#102 Write a  Python program to remove punctuation from a given string.
import string
s = "String! With. Punctuation?"
result = s.translate(str.maketrans("","", string.punctuation))
print(result)

#104  Write a  Python program that capitalizes the first letter and lowercases the remaining letters in a given string.
s = "dow jones industrial average"
print(s.title())

#7 Write a  Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
s = "The lyrics is not that poor!"
not_pos = s.find("not")
poor_pos = s.find("poor")
if not_pos != -1 and poor_pos >not_pos:
  s = s[:not_pos] + "good" + s[poor_pos +4:]
print(s)

#38 Write a Python program to count occurrences of a substring in a string.
s = "abcdabcdabcd"
sub = "abc"
print(s.count(sub))

#50  Write a Python program to split a string on the last occurrence of the delimiter.
s = "Python-Exercises- Practice"
print(s.rsplit("-", 1))

# 100  Write a Python program to split a multi-line string into a list of lines.
s = "The wait is over"
words = s.split()
has_duplicate = any(len(set(w)) < len(w) for w in words)
print(has_duplicate)

# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and  the volume of a cylinder.
import math
length, width  = 20, 15
radius, height = 7, 8
area = length * width
volume =math.pi * radius**2 * height
print(f"Diện tích HCN = {area:.2f}cm\u00b2")
print(f"Thể tích hình trụ ={volume:.3f}cm\u00b3")

#98 Write a  Python program to decapitalize the first letter of a given string.
s = "Java Script"
print(s[0].lower() + s[1:])