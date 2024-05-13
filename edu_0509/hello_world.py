print("hello world")
n=10
print(n)
n='heLLo woRLd'
# 전체 문자열의 첫글자만 대문자
print(n.capitalize()) 
print(n.upper())
print(n.lower())
# 각 문자열의 첫글자만 대문자
print(n.title())

first_name = 'ada'
last_name = 'lovelace'
# f-string
full_name = f"{first_name} {last_name}"
print(full_name.title())

# strip을 이용한 공백제거
first_name = '홍  '
last_name = '   길동'
print(first_name.strip()+last_name.strip())
