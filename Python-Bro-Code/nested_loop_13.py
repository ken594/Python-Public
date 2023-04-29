### nested loops

rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        # the end prevents the cursor moving to the next line
        print(symbol, end="")
    print()