from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # 배열 생성(사이즈)
        self.array = self.make_array(10)
        self.array_count = self.make_array(11)
        # 행과 열 길이 설정
        self.row = len(self.array)
        self.col = len(self.array[0]) if self.row > 0 else 0

        # 시작점을 배열의 중앙으로 -> size//2
        self.center = len(self.array) // 2
        # All walks start at (0, 0).
        self.x_values = [self.center]
        self.y_values = [self.center]

    def make_array(self, size):
        """2차원 배열 생성"""
        return [[0 for _ in range(size)] for _ in range(size)]

    def check_array(self, matrix):
        for row in matrix:
            for element in row:
                if element == 0:
                    return False
        return True

    def fill_walk(self):
        count = 0
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while self.check_array(self.array_count) == False:

            # Decide which direction to go, and how far to go.
            x_step = choice([1, 0, -1])
            y_step = choice([1, 0, -1])

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            if 0 > x or x > self.row:
                continue
            y = self.y_values[-1] + y_step
            if 0 > y or y > self.col:
                continue

            self.x_values.append(x)
            self.y_values.append(y)
            count += 1
            self.array_count[x][y] += 1

        self.num_points = count + 1
        print("\n".join(str(s) for s in self.array_count))
