class Setting:
    def __init__(self):
        self.config = {
            "left_pressed": False,
            "right_pressed": False,
            "ship_img_path": "images/ship.bmp",
            "alien_img_path": "images/alien.bmp",
            "ship_speed": 10,
        }

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        self.config[key] = value
