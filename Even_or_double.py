def double(num):
    """Return the number after it is doubled"""
    doubled = num * 2
    print(f"{num} times two is {doubled}!")
def is_even(num):
    if num % 2 == 0:
        print(f'{num} is an even number!')
    else:
        print(f'{num} is not an even number!')

def main():
    print("Would you like to use the EVEN function or the DOUBLE function?")
    even_or_double = input("Type EVEN or DOUBLE: ")
    if even_or_double.upper() == "EVEN":
        x = input("Choose a number for the EVEN function: ")
        is_even(int(x))
    elif even_or_double.upper() == "DOUBLE":
        y = input("Choose a number for the DOUBLE function: ")
        double(int(y))
    else:
        print("404 command not found, try again!")
        main()

if __name__ == "__main__":
    main()