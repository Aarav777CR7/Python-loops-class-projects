# ATM Cash Dispenser

print("=== ATM Cash Dispenser ===\n")

customers_served = 0

total_dispensed = 0

serving = True

while serving:


    name = input("Enter customer name: ")

    amount = int(input(f"Hello {name}! Enter withdrawal amount: "))


    if amount <= 0:

        print("Invalid amount. Please enter a positive number.\n")

        continue


    customers_served += 1

    total_dispensed += amount

    print(f"Transaction complete, {name}!\n")

    again = input("Next customer? (yes/no): ").strip().lower()

    if again != "yes":

        serving = False


print(f"\nCustomers served : {customers_served}")

print(f"Total dispensed : {total_dispensed} units")

print("ATM session closed. Goodbye!")