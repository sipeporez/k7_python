# input
message = input("아무 말이나 적어보세요:")
print(message)

# while문 - flag를 사용한 종료
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
