def main():
    try:
        number = float(input("Enter the number: "))
        root = int(input("Enter the root (e.g., 2 for square root, 3 for cube root): "))

        result = number ** (1 / root)
        print(f"The {root}th root of {number} is:", result)
    except ValueError:
        print("Please enter a valid numeric value for the number and integer value for the root.")

if __name__ == "__main__":
    main()
