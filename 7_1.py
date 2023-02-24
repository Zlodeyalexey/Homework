class Car:
    def __init__(self, color: str, count_pass_seat: int, is_baby_seat: bool, is_busy: bool = False):
        self.color = color
        self.c_p_s = count_pass_seat
        self.i_b_s = is_baby_seat
        self.is_busy = is_busy

    def __str__(self):
        return f"Car: {self.color}, {self.c_p_s}, {self.i_b_s}, {self.is_busy}"

car1 = Car('red', 4, True,True)
print(car1)