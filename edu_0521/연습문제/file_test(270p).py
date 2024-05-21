# 10-4
import os

new_path = "edu_0521/files/"
os.chdir(new_path)

print("이름을 입력하세요 : ")
guest_name = input()
with open("guest.txt", "a", encoding="utf-8") as file:
    file.write(f"{guest_name}\n")

# 10-5
flag = True
while flag:
    print("이름을 입력하세요 : (0 입력시 종료)")
    guest_name = input()
    if guest_name == "0":
        flag = False
    else:
        with open("guest_book.txt", "a", encoding="utf-8") as file:
            file.write(f"{guest_name}\n")
