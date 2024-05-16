from random import randint
from random import choice

print(randint(1, 6))

players = ["A", "B", "C", "D", "E"]
print(choice(players))


# 함수 리턴값 여러개를 일부분만 받는 법
def initialize():
    return 1, 2, 3


a, _, b = initialize()
print(a, b)


# 클래스 인스턴스에 대한 인덱싱/슬라이싱 - getitem
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]


mlist = MyList([1, 2, 3, 4, 5])
print(mlist[1:3])

# zip - 리스트 묶기
s = ["s1", "s2", "s3"]
num = [5, 3, 7]
score = zip(s, num)
# 튜플로 출력
for a, b in score:
    print(f"{a}:{b}")
