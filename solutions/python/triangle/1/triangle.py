def equilateral(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if not is_valid(sides):
        return False
    if a == b and b == c:
        return True
    else :
        return False
    


def isosceles(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if not is_valid(sides):
        return False
    if a == b or a == c or b == c:
        return True
    else :
        return False


def scalene(sides):
    a, b, c = sides
    if not is_valid(sides):
        return False
    if a != b and b != c and a != c:
        return True
    else:
        return False

def is_valid(sides):
    a, b, c = sides
    if a + b > c and b + c > a and a + c > b:
        return True
    else: False
