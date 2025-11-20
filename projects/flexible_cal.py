#IC 1st Flexible caluclator

#creating a fucntion that can chooses what you use 
def calculator(*args, operation="sum"):
    """Flexible calculator that performs sum, average, max, min, or product."""
    if operation == "sum":
        return sum(args)
    elif operation == "average":
        return statistics.mean(args)
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    elif operation == "product":
        product = 1
        for num in args:
            product *= num
        return product
    else:
        raise ValueError("Invalid operation selected.")
#defing function to findsum an didiot proofing 
def main():
    print("Welcome to the Flexible Calculator!\n")
    print("Available operations: sum, average, max, min, product\n")

    while True:
        operation = input("Which operation would you like to perform? ").lower()

        numbers = []
        print("\nEnter numbers (type 'done' when finished):")
        while True:
            entry = input("Number: ")
            if entry.lower() == "done":
                break
            try:
                numbers.append(float(entry))
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")
#making a condtional and making ssxure it can end 
#harder than then order up
#the viedo helped me a lot thank you
        if numbers:
            print(f"\nCalculating {operation} of: {', '.join(map(str, numbers))}")
            result = calculator(*numbers, operation=operation)
            print(f"Result: {result}\n")
        else:
            print("No numbers entered. Please try again.\n")

        again = input("Would you like to perform another calculation? (yes/no) ").lower()
        if again != "yes":
            print("\nThank you for using the Flexible Calculator!")
            break

if __name__ == "__main__":
    main()