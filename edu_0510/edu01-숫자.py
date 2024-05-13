age = 5
pi = 3.14
message = "hello world"
array = [1, 2, 3]
mask = "everything" or "object"
print(type(age), type(pi), type(message), type(array), type(mask))


# a = 2
# b = 4
def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)  # 몫
    print(a**b)  # a^b


# a = 3.14
# b = 1.2

# calc(a, b)

a = 3.14
b = 1_000_000_000
print(a, b)

# swap
temp = a
a = b
b = temp

print(a, b)

a, b = b, a
print(a, b)

# 정수형을 입력받아서 2 변수에 스플릿
# a, b = map(int, input("숫자 입력 : ").split())
