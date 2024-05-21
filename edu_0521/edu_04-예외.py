from pathlib import Path

path = Path(".gitignore")
try:
    contents = path.read_text(encoding="utf-8")
    print(5 / 0)
except FileNotFoundError:
    print(f"{path} 파일이 없습니다")
# except ZeroDivisionError:
#     pass
else:
    print("정상적으로 파일이 열렸습니다")
