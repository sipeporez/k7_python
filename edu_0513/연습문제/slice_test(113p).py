# 4-10
data = list(range(1, 10))

print(f"리스트의 첫 세 항목은:{data[0:3]}")
print(f"리스트의 중간 세 항목은:{data[3:6]}")
print(f"리스트의 마지막 세 항목은:{data[6:9]}")


# 4-11
pizza = ["페퍼로니", "치즈", "불고기"]
pizza.append("콤비네이션")
friend_pizzas = ["포테이토"]

print(f"내가 좋아하는 피자는:")
for i in pizza:
    print(i)

print(f"친구가 좋아하는 피자는:")
for i in friend_pizzas:
    print(i)
