from .fizz_buzz import fizz_buzz, fizz_buzz_runner

def test_one_gives_one():
    assert fizz_buzz(1) == "1"

def test_two_gives_two():
    assert fizz_buzz(2) == "2"

def test_three_gives_fizz():
    assert fizz_buzz(3) == "Fizz"

def test_five_gives_buzz():
    assert fizz_buzz(5) == "Buzz"
    
def test_15_gives_fizzbuzz():
    assert fizz_buzz(15) == "FizzBuzz"

def test_17_gives_17():
    assert fizz_buzz(17) == "17"

def test_21_gives_Fizz():
    assert fizz_buzz(21) == "Fizz"

def test_0_to_16():
    assert fizz_buzz_runner(16) == [
                                    "1","2","Fizz",
                                    "4","Buzz","Fizz",
                                    "7","8","Fizz","Buzz",
                                    "11","Fizz","13",
                                    "14","FizzBuzz","16"
                                    ]

