def fizz_buzz(input):
    return str(fizz(input) + buzz(input) or input)

def fizz(input):
    return "Fizz" if is_fizz(input) else ""

def buzz(input):
    return "Buzz" if is_buzz(input) else ""

def is_fizz(input):
    return input % 3 == 0

def is_buzz(input):
    return input % 5 == 0

def fizz_buzz_runner(count):
    return [fizz_buzz(number + 1) for number in range(count)]
