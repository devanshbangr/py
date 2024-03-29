def main():
    # Creating a dictionary of tuples
    employee_data = {
        ('John', 'Doe'): {'age': 30, 'position': 'Manager'},
        ('Alice', 'Smith'): {'age': 25, 'position': 'Engineer'},
        ('Bob', 'Johnson'): {'age': 35, 'position': 'Developer'}
    }

    # Accessing elements of the dictionary using tuples as keys
    print("Employee Data:")
    for name, info in employee_data.items():
        first_name, last_name = name
        print(f"{first_name} {last_name}:")
        print("  Age:", info['age'])
        print("  Position:", info['position'])
        print()

if __name__ == "__main__":
    main()
