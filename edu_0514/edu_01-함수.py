# immutable 객체 테스트
def modify_string(s, num):
    s = s + "world"
    num += 10
    print(f"함수 내 출력 : {s, num}")


st = "hello"
num = 10
modify_string(st, num)
print(f"메인 출력 : {st, num}")

# 모듈
import pizza
from pizza import make_pizza as pz

pz(16, "pepperoni")
pz(12, "mushrooms", "green peppers", "extra cheese")


### Part 1 - 함수 인자 전달
def five_times(func):
    for i in range(5):
        func()


def print_hello():
    print("Hello")


# 함수를 매개변수로 전달
five_times(print_hello)


### Part 2 - 함수 인자 여러개 전달
def added(x, y):
    return x + y


def apply_oper(operation, x, y):
    return operation(x, y)


result = apply_oper(added, 3, 4)
print(result)


### Part 3 - map / filter
def power(item):
    return item**2


def under_three(item):
    return item < 3


lst = [1, 2, 3, 4, 5]
map_lst = map(power, lst)
print(list(map_lst))
filter_lst = filter(under_three, lst)
print(list(filter_lst))

### Part 4 - 람다식
m_lst = list(map(lambda x: x**3, lst))
print(m_lst)
