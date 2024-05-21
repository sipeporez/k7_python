from pathlib import Path

# 파일 생성 및 쓰기
with open("edu_0521/실습/example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

print("File created and written successfully.")

# path를 사용하는 경우 덮어쓰기가 됨
path = Path("edu_0521/실습/example.txt")
path.write_text("path 객체를 사용한 쓰기")


# 파일에 내용 추가하기
with open("edu_0521/실습/example.txt", "a") as file:
    file.write("Adding a new line.\n")
    file.write("Appending another line.\n")

print("Content appended to the file successfully.")

# 새로운 파일 생성하기
try:
    with open("edu_0521/실습/new_file.txt", "x") as file:
        file.write("This is a newly created file.\n")
    print("New file created and written successfully.")
except FileExistsError:
    print("File already exists.")
