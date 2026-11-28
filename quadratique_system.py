import math


def solve_in_R(a, b, c):
    if a == 0:
        if b == 0:
            return "No unique solution"
        return -c / b
    delta = (b**2) - (4 * a * c)


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2
elif delta == 0:
    return -b / (2 * a)
else:
    return "No real solutions"
print(solve_in_R(2, 2, -4))
