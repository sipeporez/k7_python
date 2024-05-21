# 파일 생성
from pathlib import Path
import os

print(f"현재 경로 : {os.getcwd()}")  # 현재 디렉토리를 출력

new_path = "edu_0521/files/"
os.chdir(new_path)  # 디렉토리 변경

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

print(f"파일 내용 : {contents}")

path = Path("programming.txt")
path.write_text(contents)
print(f"파일 쓰기 : {path}")

readfile = path.read_text()
print(f"파일 읽기 : {readfile}")
