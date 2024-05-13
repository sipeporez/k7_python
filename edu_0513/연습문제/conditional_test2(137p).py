# 5-3

alien_color = "green"

if alien_color == "green":
    print("플레이어 5점 획득")

# 5-4
alien_color = "yellow"

if alien_color == "green":
    print("플레이어 5점 획득")
else:
    print("플레이어 10점 획득")

if alien_color == "green":
    print("플레이어 5점 획득")
if alien_color != "green":
    print("플레이어 10점 획득")

# 5-5
if alien_color == "green":
    print("플레이어 5점 획득")
elif alien_color == "yellow":
    print("플레이어 10점 획득")
else:
    print("플레이어 15점 획득")

# 5-6
age = 64

if age < 2:
    print("baby")
elif (age >= 2) and (age < 4):
    print("toddler")
elif (age >= 4) and (age < 13):
    print("kid")
elif (age >= 13) and (age < 20):
    print("teenager")
elif (age >= 20) and (age < 65):
    print("adult")
elif age >= 65:
    print("elder")

# 5-7
favorite_fruits = ["딸기", "바나나", "귤"]
if "딸기" in favorite_fruits:
    print("당신은 딸기를 좋아합니다.")
if "바나나" in favorite_fruits:
    print("당신은 바나나를 좋아합니다.")
if "사과" not in favorite_fruits:
    print("당신은 사과를 좋아하지 않습니다.")
if "귤" in favorite_fruits:
    print("당신은 귤을 좋아합니다.")
if "배" in favorite_fruits:
    print("당신은 배를 좋아합니다.")
