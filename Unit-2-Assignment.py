def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

def main():
    """Main entry function"""
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

def test_add_numbers():
    """Unit test for add_numbers function"""
    assert add_numbers(3, 5) == 8
    assert add_numbers(-1, 1) == 0
    assert add_numbers(2.5, 7.5) == 10.0
    assert add_numbers(0, 0) == 0
    print("All tests pass for add_numbers function!")

if __name__ == "__main__":
    main()
    test_add_numbers()
