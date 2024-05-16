from Person import *
import Dept


class Student(Person):
    def __init__(self, pid, pname, age, sid, syear, sdept):
        self.sid = sid
        self.syear = syear
        self.sdept = sdept
        super().__init__(pid, pname, age)

    def print_student(self):
        return f"{Person.print_person(data)}\nsid : {self.sid}\nsyear : {self.syear}\nsdept : {self.sdept}"


s1 = Student("111111", "ran", 36, "sid01", 2023, Dept.dept[0])
s2 = Student("555555", "my", 27, "sid01", 2022, Dept.dept[1])
s3 = Student("888888", "jang", 33, "sid01", 2021, Dept.dept[2])
s4 = Student("232561", "lee", 14, "sid01", 2020, Dept.dept[3])
s5 = Student("964851", "gyu", 42, "sid01", 2024, Dept.dept[4])

slist = [s1, s2, s3, s4, s5]
total_list = [*slist, *plist]
print(total_list)
for idx, data in enumerate(total_list):
    if isinstance(data, Student):
        print(f"Student {idx+1}번째 출력:\n{data.print_student()}\n")
    elif isinstance(data, Person):
        print(f"Person {idx+1}번째 출력:\n{Person.print_person(data)}\n")
