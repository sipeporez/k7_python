# 3-4
guest_list = ["a", "b", "c", "d", "e"]

for guest in guest_list:
    print(f"{guest}, 식사에 초대합니다.")

# 3-5

print(f"{guest_list[3]}, 식사에 참가할 수 없습니다.")
guest_list.remove(guest_list[3])
for guest in guest_list:
    print(f"{guest}, 식사에 다시 초대합니다.")

# 3-6
print("더 큰 테이블을 찾았습니다.")
guest_list.insert(0, "Z")
guest_list.insert(3, "Y")
guest_list.append("T")
for guest in guest_list:
    print(f"{guest}, 더 큰 테이블에 초대합니다.")

# 3-7
print("2명만 초대 가능합니다.")
for i in range(0, 5):
    print(guest_list.pop(), "죄송합니다")

print(f"{guest_list} 는 취소되지 않았습니다.")
del guest_list[0]
del guest_list[1]

print(guest_list)
