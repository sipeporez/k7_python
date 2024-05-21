# 파일 읽기, 경로 읽기 및 변경
from pathlib import Path
import os

print(f"현재 경로 : {os.getcwd()}")  # 현재 디렉토리를 출력

new_path = "edu_0521/files/"
os.chdir(new_path)  # 디렉토리 변경

print(f"변경 후 경로 : {os.getcwd()}")  # 변경 후 디렉토리를 출력

path = Path("pi_digits.txt")

contents = path.read_text()  # 파일을 읽어서 contents에 저장 (리스트 타입)
lines = contents.splitlines()  # 저장된 내용을 줄마다 잘라서 lines에 저장
pi_string = ""  # 출력을 바꾸기 위한 변수 선언

for line in lines:
    pi_string += line.strip()  # 공백을 자르고 저장
    print(f"line 출력 : {line}")
    print(f"pi_string 출력 : {pi_string}")

# 100만자리 pi 출력

path2 = Path("pi_million_digits.txt")

contents2 = path2.read_text()
lines2 = contents2.splitlines()
pi_string2 = ""

for line2 in lines2:
    pi_string2 += line2.lstrip()

print(f"lines2 길이 : {len(lines2)}")
print(f"pi_string2 출력 : {pi_string2[:52]}...")
print(f"pi_string2 길이 : {len(pi_string2)}")
