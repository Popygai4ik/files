class Vector:
    def __init__(self, x_coor_1: float, y_coor_1: float, x_coor_2: float, y_coor_2: float):
        self.x_coors = [x_coor_1, x_coor_2]
        self.y_coors = [y_coor_1, y_coor_2]
        self.x1 = x_coor_1
        self.y1 = y_coor_1
        self.x2 = x_coor_2
        self.y2 = y_coor_2
        self.del_x = x_coor_2 - x_coor_1
        self.del_y = y_coor_2 - y_coor_1

    def __sub__(self, other):
        return Vector(self.x1, self.y1, self.x2 - (other.x2 - other.x1), self.y2 - (other.y2 - other.y1))

    def __len__(self):
        return int(((self.del_x ** 2 + self.del_y ** 2)**0.5))
    def __add__(self, other):
        x_coor_1 = self.x_coors[0]
        x_coor_2 = self.x_coors[1] + (other.x_coors[1] - other.x_coors[0])
        y_coor_1 = self.y_coors[0]
        y_coor_2 = self.y_coors[1] + (other.y_coors[1] - other.y_coors[0])
        return Vector(x_coor_1, y_coor_1, x_coor_2, y_coor_2)

    def __mul__(self, other):
        if isinstance(other, Vector):

            return Vector(self.x1, self.y1, self.x2 * other.x2, self.y2 * other.y2)
        elif isinstance(other, (int, float)):

            return Vector(self.x1, self.y1, self.x2 * other, self.y2 *other)
    def __str__(self):
        return f"Вектор(\t Начало ({self.x1}, {self.y1})\t Конец ({self.x2}, {self.y2}))"


a = Vector(0, 0, 3, 4)
b = Vector(0, 0, 3, 6)
# print(a + b)

# print(a - b)
# print(len(a))
print(a)
print(b)
print(a * b)