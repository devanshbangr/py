def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if num1 < 0 or num2 < 0:
            raise ValueError("Please enter non-negative integers.")

        result = gcd(num1, num2)
        print("The GCD of", num1, "and", num2, "is:", result)
    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()
