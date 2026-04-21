def is_armstrong_number(number):

    digits = [int(d) for d in str(number)]
    power_number = len(digits)
    total = 0
    for d in digits:
        total += d**power_number
    if total == number:
            return True
    else:
            return False

