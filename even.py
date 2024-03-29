def is_even(number):
    return number % 2 == 0

def main():
    try:
        number = int(input("Enter a number: "))
        if is_even(number):
            print(number, "is an even number.")
        else:
            print(number, "is not an even number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
