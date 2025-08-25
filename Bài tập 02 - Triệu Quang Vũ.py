# 1. Guess The Number Game:
# -we will generate a random number with the help of randint() function from 1 to 100 and ask the user to guess it.
# -After every guess, the user will be told if the number is above or below the randomly generated number.
# -The user will win if they guess the number maximum five attempts.
# -Ask the user to stop or continue playing again.
# ***
# Add another situations like:
# level of game (hard (guess 3 times), medium (6 times), easy (10 times)
# assume that you have 100$, each game you spent 5$. Play game until you choose stop, report the game you win/lost and amount you have.
import random # dùng để sinh số ngẫu nhiên
def play_game(level):
    # số lần đoán theo độ khó
    if level =="easy":
        attempts = 10
    elif level == "medium":
        attempts = 6
    elif level == "hard":
        attempts = 3
    else:
        print("Chọn sai mức độ! Mặc định là easy.")
        attempts =10
    #sinh số ngẫu nhiên từ 1 -> 100
    secret = random.randint (1, 100)
    print(f"\n Tôi đã chọn 1 số từ 1 đến 100.")
    print(f"Bạn có {attempts} lần đoán.")
    # Cho người chơi đoán
    for i in range (1, attempts +1):
        guess = int(input(f"Lần {i} - Nhập số bạn đoán: "))
        if guess == secret:
            print("Chúc mừng! Bạn đã đoán đúng.")
            return True # Thắng
        elif guess < secret:
            print(" Số bạn đoán nhỏ hơn số bí mật.")
        else:
            print("Số bạn đoán lớn hơn số bí mật.")
    print(f" Bạn đã thua. Số bí mật là {secret}.")
    return False # Thua
#---Main game loop---#
money = 100
win_count = 0
lose_count = 0
print("Chào mừng bạn đến với trò chơi Đoán Số !")
print("Bạn có 100$. Mỗi ván chơi mất 5$.")
while money >=50:
     print("\n Chọn mức độ chơi:")
     print("1. Easy (10 lần đoán) ")
     print("2. Medium (6 lần đoán) ")
     print("3. Hard (3 lần đoán) ")
     choice = input("Nhập 1/2/3: ")
     if choice == "1":
         level = "easy"
     elif choice == "2":
         level = "medium"
     elif choice == "3":
         level = "hard"
     else:
         print("Lựa chọn không hợp lệ. Mặc định: Easy")
         level = "easy"
     # Trừ tiền để chơi
     money -=5
     # Chơi game
     result = play_game(level)
     if result:
         win_count +=1
     else:
         lose_count -=1
     print(f" Số tiền còn lại: {money}$")
     #Hỏi người chơi có muốn chơi tiếp không
     again = input("Bạn có muốn chơi tiếp không? (y/n): ").lower()
     if again != "y":
         break
#---Kết thúc trò chơi---
print("\n === KẾT QUẢ ===")
print(f"Số trận thắng: {win_count}")
print(f"Số trận thua: {lose_count}")
print(f"Số tiền còn lại: {money}$")
print("Cảm ơn bạn đã chơi! ")

#==================================================================================================#
# .Write a game that simulate rolling a pair of dice.
# -If the sum of two faces is greater than 5 à “Tài”
# -Otherwise  à “Xỉu”
# -User ask for guessing “Tài” or “Xỉu”
# -Match the results
# -After one turn, ask user for continue playing game.
# -**** Extend the game by asking the user to enter an amount of money, then continue playing until the user runs out of money or the user stops playing. Statistics of results.


import random #dùng để gieo xúc xắc
print("Chào mừng bạn đến với game Tài Xỉu")
#vốn ban đầu
money = int(input("Nhập số tiền bạn muốn chơi: "))
win_count = 0
lose_count =0
#vòng lặp chính
while money > 0:
    print("\nBạn còn", money, "$")
    guess = input("Bạn đoán Tài hay Xỉu?").lower()
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    total = dice1 +dice2
    print("Kết quả xúc xắc: ", dice1, "+", dice2, "=", total )
    # Xác định tài hay xỉu
    if total > 5:
        result = "tài"
    else:
        result = "xỉu"
    print("Kết quả là: ", result.capitalize())
    #So sánh dự đoán
    if guess == result:
        print("Bạn đã thắng!")
        win_count +=1
        money +=10 # thắng được cộng 10$
    else:
        print("Bạn đã thua! ")
        lose_count +=1
        money -=10 #thua bị trừ 10$
    #kiểm tra còn tiền không
    if money <=0:
        print("\nBạn đã hết tiền, trò chơi kết thúc! ")
        break
    #hỏi người chơi có muốn chơi tiếp không:>
    cont = input("Bạn có muốn chơi tiếp không ? (y/n): ").lower()
    if cont !="y":
        break
print("\nThống kê kết quả")
print("Số trận thắng:", win_count)
print("Số trận thua:", lose_count)
print("Số tiền còn lại:", money, "$")
print("Cảm ơn bạn đã chơi!")