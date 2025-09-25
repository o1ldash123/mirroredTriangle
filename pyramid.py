rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
        # Print leading spaces
        for _ in range(rows - i):
            print(" ", end="")
        # Print asterisks
        for _ in range(i):
            print("*", end="")
        print() 