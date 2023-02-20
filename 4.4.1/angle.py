from math import sin, pi

class Angle:
    degree = 0
    minute = 0
    second = 0

    def __init__(self, degree_: int, minute_: int, second_: int):
        if second_ < 0 or second_ >= 60:
            minute_ += (second_ - second_ % 60) // 60
            second_ %= 60
        if minute_ < 0 or minute_ >= 60:
            degree_ += (minute_ - minute_ % 60) // 60
            minute_ %= 60

        self.degree, self.minute, self.second = degree_, minute_, second_

    def __add__(self, other):
        return Angle(self.degree + other.degree, self.minute + other.minute, self.second + other.second)

    def __sub__(self, other):
        sign = -1 if other.degree >= 0 else 1
        return Angle(self.degree + sign * other.degree, self.minute + sign * other.minute, self.second + sign * other.second)
        
    def __str__(self):
        str_degree = '*'
        str_minute = '\''
        str_second = '\'\''
        return f'{self.degree}{str_degree}{self.minute}{str_minute}{self.second}{str_second}'

    def tex(self):
        tex_degree = r' ^{\circ}'
        tex_minute = '\''
        tex_second = '\'\''
        return f'{self.degree}{tex_degree}{self.minute}{tex_minute}{self.second}{tex_second}'

def c_sin(a: Angle):
    return sin((a.degree + a.minute / 60 + a.second / 360) * pi / 180)