class Dog2:
    """클래스 Dog 정의"""

    def __init__(self, name, age):
        """클래스 Dog 생성자"""
        self.name = name
        self.age = age

    def sit(self):
        """앉기"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """구르기"""
        print(f"{self.name} rolled over.")


myDog = Dog2("hong", 10)
myDog.sit()

myDog.roll_over()
