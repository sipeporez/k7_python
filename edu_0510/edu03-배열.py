data = [1, 2, 3, 3, 3]
print(data, type(data))

# data = list()
# print(data, type(data))

print(data[0])
print(data[1])
print(data[2])

print(len(data))

data.append(6)
data.append(7)
data.append(8)

print(data[0:8])
print(len(data))

data[3] = 9
data[4] = 10
print(data, len(data), sum(data), min(data), max(data))

data = list(range(10, 0, -1))
print(data, type(data), sorted(data))

# 입력 : 10 9 8 7 6 5 4 3 2 1
# 출력 : 합계, 최댓값, 최솟값, 오름차순 정렬

# input은 입력받기, split은 공백 기준으로 자르기
# 입력받은 데이터를 int 타입으로 매핑 후 리스트로 변환
# data = list(map(int, input().split()))
# print(data, type(data), type(data[0]))
# print(sum(data), max(data), min(data), sorted(data))

data = [1, 2, 3.14, "hello", len, range(5)]
for d in data:
    print(d, type(d))

# 배열의 길이 반환
print(data[-1])

# 배열 뒤집기
print(data[::-1])

# 뒤집기를 이용한 회문 검사
msg = "기러기"
print(msg == msg[::-1])
