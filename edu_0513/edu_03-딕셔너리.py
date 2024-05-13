# 딕셔너리 기본 문법
alien_0 = {"color": "green", "points": 5}
print(alien_0, alien_0["color"])

# 딕셔너리 키 삭제 (del)
del alien_0["points"]
print(alien_0)

# 딕셔너리 가져오기 (get)
print(alien_0.get("points", "해당 키가 없음"))

# 딕셔너리 순회 (key,value in .items() .keys() .values())
user = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")
print()
for key in user.keys():
    print(key)
print()
for value in user.values():
    print(value)

# 중첩
data = [{"a": "b"}, {"c": "d"}, {"e": "f"}]
data2 = {"[1, 2, 3]": "[4,5,6]", "[3, 4, 5]": "[6, 7, 8]"}

for li in data:
    print(li.keys())
    print(li.values())

for key in data2.items():
    print(key)


# 딕셔너리 중첩 반복 순회
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, lang in favorite_languages.items():
    print(f"\n{name.title()} is like ")
    for language in lang:
        print(f"\t{language.title()}")

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
        "job": "scientist",
        "salay": 1000,
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
        "job": "artist",
        "salay": 1200,
    },
}
for username, user_info in users.items():
    print(f"\n{username.title()}")
    for info in user_info.values():
        if type(info) == int:
            print(f"\t{info}")
        else:
            print(f"\t{info.title()}")
