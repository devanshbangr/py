def main():
    try:
        base = float(input("Enter the base value: "))
        exponent = float(input("Enter the exponent value: "))

        result = base ** exponent
        print("The exponential form of", base, "raised to the power of", exponent, "is:", result)
    except ValueError:
        print("Please enter valid numeric values for base and exponent.")

if __name__ == "__main__":
    main()
