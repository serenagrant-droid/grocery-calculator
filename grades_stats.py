def main():
    total = 0.0
    max_grade = float('-inf')   # Start with the smallest possible number
    min_grade = float('inf')    # Start with the largest possible number

    print("Enter 10 grades below:")

    for i in range(1, 11):
        while True:
            try:
                grade = float(input(f"Enter grade #{i}: "))
                break  # valid input, leave loop
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")

        total += grade

        if grade > max_grade:
            max_grade = grade

        if grade < min_grade:
            min_grade = grade

    average = total / 10

    print("\n----- RESULTS -----")
    print(f"Average grade: {average:.2f}")
    print(f"Maximum grade: {max_grade:.2f}")
    print(f"Minimum grade: {min_grade:.2f}")


# Run the program
main()
