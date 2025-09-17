# 1.to handle a ZeroDivisionError exception when dividing a number by zero.
def divide(a, b):
    try:
        result = a / b
        print("Kết quả:", result)
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho ).")
divide(10, 2)
divide(8, 0)

# 2.that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def input_interger():
    try:
        num = int(input("Nhập một số nguyên: "))
        print("Bạn đã nhập số:" , num)
    except ValueError:
        print("Lỗi: Giá trị nhập không phải số nguyên!")
input_interger()
# 3.that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def input_two_numbers():
    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        print("Tổng hai số là:", a + b)
    except ValueError:
        raise TypeError("Lỗi: Cả hai giá trị nhập vào phải là số. ")
try:
    input_two_numbers()
except TypeError as e:
    print(e)

# 4.that executes an operation on a list and handles an IndexError exception if the index is out of range.
def access_list_element():
    my_list = [10, 20, 30, 40, 50]
    try:
        index = int(input("Nhập vị trí phần tử (0 - 4): "))
        print("Phần tử tại vị trí", index, "là:", my_list[index])
    except IndexError:
        print("Lỗi: Chỉ số vượt quá phạm vi danh sách!")
access_list_element()
# 5.that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
def input_with_interrupt():
    try:
        num = input("Nhập một số: ")
        print("Bạn đã nhập:", num)
    except KeyboardInterrupt:
        print("\nNgười dùng đã hủy nhập(Ctrl + C).")
# 6.that executes division and handles an ArithmeticError exception if there is an arithmetic error.
def safe_division(a, b):
    try:
        result = a / b
        print("Kết quả:", result)
    except ArithmeticError as e:
        print("Lỗi số học: ", e)
safe_division(10, 2)
safe_division(8, 0)