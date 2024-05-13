# 구글 검색, chatGPT 사용하여 다음 코드를 완성
import itertools
import random

# 빈 리스트 생성
random_numbers = []

# 난수를 20개 생성하여 리스트에 추가
for _ in range(20):
    random_numbers.append((random.randint(1, 101)))
# 저장된 리스트 출력
print(f"난수 생성 = {random_numbers}")
# s 다음에 숫자를 가진 변수들을 생성하여 리스트에 저장하는 예제

# 빈 리스트 생성
string_list = []

# s 다음에 숫자를 가진 변수들 생성하여 리스트에 추가: s1, s2, s3 등을 생성
for i in range(1, 21):
    string_list.append(f"s{i}")
# 저장된 리스트 출력
print(f"sno 리스트 = {string_list}")

students = string_list
scores = random_numbers

# students, scores로 구성된 딕셔너리를 만든다
for _ in range(20):
    score_dic = dict(zip(students, scores))

print(f"학번과 점수 딕셔너리={score_dic}")
# 점수를 기준으로 내림차순으로 정렬한 튜플 리스트 생성
sorted_scores = sorted(score_dic.items(), key=lambda value: value[1], reverse=True)

# 정렬된 튜플 리스트를 다른 딕셔너리에 저장
sorted_score_dic = dict(sorted_scores)

# 결과 출력
print(f"점수로 정렬된 딕셔너리= {sorted_score_dic}")
# 정렬된 튜플 리스트에서 상위 5개 추출하여 리스트로 저장
# 상위 5개 추출하여 딕셔너리로 저장

top_5 = dict(itertools.islice(sorted_score_dic.items(), 5))

# 결과 출력
print(f"상위 5개= {top_5}")
# 딕셔너리의 키-값 쌍을 튜플로 묶어 리스트에 추가
score_list = list(zip(top_5.keys(), top_5.values()))

# 결과 출력
print(f"리스트로 변환된 딕셔너리: {score_list}")

# 딕셔너리의 각 요소를 enumerate를 사용하여 변환
transformed_score_dic = {index + 1: value for index, value in enumerate(score_list)}
# 결과 출력
print(f"변환된 딕셔너리: {transformed_score_dic}")
