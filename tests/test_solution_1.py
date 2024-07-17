# test_solution.py
from solutions.sample_1 import add_number

def test_add_number():
    assert add_number(1, 2) == 3
    assert add_number(-1, 1) == 0
    assert add_number(0, 0) == 0
    assert add_number(123, 456) == 579
    print("All tests passed!")

if __name__ == "__main__":
    test_add_number()
