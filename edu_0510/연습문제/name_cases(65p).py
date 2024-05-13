# 2-3
name = "에릭"
msg = "안녕하세요. "
msg2 = "오늘 파이썬 배워 보는게 어떨까요?"

print(f"{msg}{name}, {msg2}")

# 2-4
name = "ada loverace"
print(name.upper(), name.lower(), name.capitalize())

# 2-5
print(
    f'알베르트 아인슈타인, "한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다.'
)

# 2-6
famous_name = "알베르트 아인슈타인"
message = (
    "한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전해 본 적이 없는 사람이다."
)
print(f'{famous_name}, "{message}')

# 2-7
name = "     ada\tlove\nrace     "
print(name.lstrip().rstrip().strip())
