class Person:
    def __init__(self, pid, pname, age):
        self.pid = pid
        self.pname = pname
        self.age = age

    def print_person(self):
        """Person 출력"""
        return f"pid : {self.pid}\npname : {self.pname}\nage : {self.age}"


p1 = Person("202020", "hong", 25)
p2 = Person("303030", "kim", 21)
p3 = Person("404040", "dg", 17)
p4 = Person("505050", "tttt", 34)
p5 = Person("606060", "kyr", 51)

plist = [p1, p2, p3, p4, p5]

for idx, i in enumerate(plist):
    print(f"Person {idx+1}번째 출력:\n{i.print_person()}\n")
