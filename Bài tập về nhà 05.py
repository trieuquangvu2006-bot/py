# 1.Write a Python program to find the maximum and minimum values in a set.
a = {1, 3, 4, 5, 6, 7, 8, 9}
print(f"Giá trị lớn nhất là {max(a)}")
b = {1, 2, 34, 5, 6, 7, 8, 9}
print(f"Giá trị nhỏ nhất là {min(b)}")
# 2.Write a Python program to check if a given value is present in a set or not.
a = {"Python", "C++", "Java"}
value = "Python"
if value in a:
    print(f" Giá trị {value} có nằm trong set")
else:
    print(f" Giá trị {value} không nằm trong set")
# 3.Write a Python program to check if two given sets have no elements in common.
 # Hàm "isdisjoint" trả về True nếu như không có phần tử chung và trả về False nếu có phần tử chung
a = {1, 2, 3, "Hello World", "Xin Chào", "Ahihi"}
b = {1, 2, 5, "Vietnamese", "À nhon xê ô", "Ahihi"}
if a.isdisjoint(b):
    print("Hai set không có phần tử chung")
else:
    print("Hai set CÓ phần tử chung")
# 4.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
words = ["Chuối","Chuối","Xoài","Xoài", "Măng cụt", "Măng cụt", "Táo", "Xoài", "Măng cụt"]
unique_words = set(words)
print(f"Tất cả các từ: {unique_words}")
for w in unique_words:
    print(w,":", words.count(w))
# 5.Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {12, 3, 4, 5, 98, 43, 76, 8}
missing_in_b = a.difference(b)
print(f"Có trong a nhưng không có trong b là: {missing_in_b}")
missing_in_a = b.difference(a)
print(f"Có trong b nhưng không có trong a là: {missing_in_a}")

print("-" * 200)

employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}

dept_employees = {}

for emp_id, info in employees.items():
    dept = info["department"]  # Lấy tên phòng ban

    if dept not in dept_employees:
        dept_employees[dept] = {}

    dept_employees[dept][emp_id] = {
        "name": info["name"],
        "salary": info["salary"]
    }
print("Dictionary nhóm theo phòng ban:")
print(dept_employees)
