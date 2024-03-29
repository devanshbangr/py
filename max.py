def main():
    try:
        num_list = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
        if num_list:
            largest_number = max(num_list)
            print("The largest number in the list is:", largest_number)
        else:
            print("The list is empty.")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
