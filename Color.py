class Colors:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b}) "

    def __eq__(self, other):
        if isinstance(other, Colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented
red = Colors('красный', 255, 0, 0)
green = Colors('зеленый', 0, 255, 0)
otherRed = Colors('другой красный', 255, 0, 0)

print(otherRed)
print(red)
print(green)

print(red == green)
print(red == otherRed)
print(green)