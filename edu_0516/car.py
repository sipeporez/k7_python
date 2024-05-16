# import용 .py 파일 / 클래스 변수와 메소드 추가


class Car2:
    """자동차를 표현하는 클래스"""

    # 클래스 변수 count
    count = 0

    # 클래스 메소드
    @classmethod
    def printing(self):
        print(f"클래스 메소드 출력 : {Car2.count}")

    def __init__(self, make, model, year, color):
        """속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.odometer = 0

    # 던더 메소드, 인스턴스를 str로 표현
    def __str__(self):
        return f"[{self.make},{self.model}]"

    def get_descriptive_name(self):
        """뜻이 있고 깔끔한 이름 반환"""
        long_name = f"{self.year}년식 {self.make} {self.model} {self.color}"
        return long_name.title()

    def read_odometer(self):
        """주행거리 출력"""
        print(f"주행 거리:{self.odometer}")

    def update_odometer(self, km):
        """주행거리 갱신"""
        if km >= self.odometer:
            self.odometer = km
        else:
            print("주행거리는 되돌릴 수 없음")

    def fill_gas_tank(self):
        print("가스탱크 충전")


# 클래스 상속
class ElecCar(Car2):
    # init 호출 = 상위 클래스의 생성자 호출
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)
        # 배터리 클래스 생성 (합성)
        self.battery = Battery()

    # 메소드 오버라이딩
    def fill_gas_tank(self):
        return "전기차는 가스를 사용하지 않음"


# 클래스 합성 (composition)
class Battery:
    """전기차 배터리 표현 클래스(합성 composition)"""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def battery_capa(self):
        return f"배터리 크기 : {self.battery_size}"
