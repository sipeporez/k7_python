from random import randint, choices


# 9-13
class Die:
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        return randint(1, self.side)

    def roll_die_10(self):
        return randint(1, 10)

    def roll_die_20(self):
        return randint(1, 20)


dice = Die()
print("6면체 주사위 10번")
for _ in range(10):
    print(dice.roll_die())
print("10면체 주사위 10번")
for _ in range(10):
    print(dice.roll_die_10())
print("20면체 주사위 10번")
for _ in range(10):
    print(dice.roll_die_20())

# 9-14
lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

winner = choices(lotto, k=4)
print(f"복권 당첨번호 : {winner}")

# 9-15
win = True
count = 0
my_ticket = []
while win:
    my_ticket.append(choices(lotto, k=4))
    if winner == my_ticket[count]:
        print(f"내 티켓 : {my_ticket[count]}")
        print(f"{count}번 만에 당첨됨")
        win = False
    count += 1
