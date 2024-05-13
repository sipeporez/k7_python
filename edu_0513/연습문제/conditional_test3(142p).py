# 5-8
user_name = ["admin", "A", "B", "C", "D"]

for i in user_name:
    if i == "admin":
        print("관리자님 안녕하세요.")
    else:
        print(f"{i}님 안녕하세요.")

# 5-9
user_name = []
if not user_name:
    print("사용자가 있어야 합니다.")
else:
    print(f"사용자 리스트 : {user_name}")

# 5-10
current_user = ["admin", "A", "B", "C", "D"]
new_user = ["a", "b", "G", "H", "I"]

current_user_lower = []

for i in current_user:
    current_user_lower.append(i.lower())
for i in new_user:
    if i in current_user_lower:
        print("새로운 사용자 이름을 입력하세요.")
    else:
        print("해당 이름은 사용 가능합니다.")

# 5-11
numb = list(range(1, 10))

for i in numb:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print(f"{i}th")
