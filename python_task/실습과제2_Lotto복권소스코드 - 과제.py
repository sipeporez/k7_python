# 수정할 것
# 1. 당첨번호 생성
# 2. 생성된 당첨번호를 리스트로 저장 후 정렬
# 3. 100장을 묶어서 리스트로 저장 후 리스트의 요소 1개씩 꺼내서(1장) 당첨 비교
# 4. 당첨 비교 반복문 -> 함수로 구현

# 아래는 파이썬 세트를 사용하여 로또 복권 6개 번호와 보너스 번호를 100장 발행하여 세트에 저장하는 코드입니다.
import random


# def check_winner(
#     lotto_numbers, winning_numbers, lotto_bonus_number, winning_bonus_number
# ):
#     if lotto_numbers == winning_numbers:
#         print(f"{idx}번째 로또 복권: 1등 당첨!")
#     elif (
#         len(lotto_numbers.intersection(winning_numbers)) == 5
#         and lotto_bonus_number == winning_bonus_number
#     ):
#         print(f"{idx}번째 로또 복권: 2등 당첨! (5개 일치 + 보너스 번호 일치)")
#     elif len(lotto_numbers.intersection(winning_numbers)) == 5:
#         print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치)")
#     elif len(lotto_numbers.intersection(winning_numbers)) == 4:
#         print(f"{idx}번째 로또 복권: 4등 당첨! (4개 일치)")
#     elif len(lotto_numbers.intersection(winning_numbers)) == 3:
#         print(f"{idx}번째 로또 복권: 5등 당첨! (3개 일치)")
#     else:
#         print(f"{idx}번째 로또 복권: 꽝")


def check_win(llist, winning_numbers, winning_bonus_number):
    for idx, (num_set, bonus) in enumerate(llist):
        if num_set == winning_numbers:
            print(f"{idx+1}번째 로또 복권: 1등 당첨!")
        elif (
            len(num_set.intersection(winning_numbers)) == 5
            and bonus == winning_bonus_number
        ):
            print(f"{idx+1}번째 로또 복권: 2등 당첨! (5개 일치 + 보너스 번호 일치)")
        elif len(num_set.intersection(winning_numbers)) == 5:
            print(f"{idx+1}번째 로또 복권: 3등 당첨! (5개 일치)")
        elif len(num_set.intersection(winning_numbers)) == 4:
            print(f"{idx+1}번째 로또 복권: 4등 당첨! (4개 일치)")
        elif len(num_set.intersection(winning_numbers)) == 3:
            print(f"{idx+1}번째 로또 복권: 5등 당첨! (3개 일치)")
        else:
            print(f"{idx+1}번째 로또 복권: 꽝")


# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))

    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음)
    lotto_numbers = set(random.sample(numbers, 6))

    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)

    return lotto_numbers, bonus_number


# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers()
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)

lotto_list = []
# 100장의 로또 번호 생성하여 당첨 여부 판별
for idx in range(1, 101):
    lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
    # 튜플형으로 데이터 삽입
    lotto_list.append((lotto_numbers, lotto_bonus_number))
    # check_winner(
    #     lotto_numbers, winning_numbers, lotto_bonus_number, winning_bonus_number
    # )
check_win(lotto_list, winning_numbers, winning_bonus_number)
