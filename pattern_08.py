n = int(input('Enter the value for n: '))
for row in range(1, n+1):
    for col in range(row, 0, -1):
        print(col, end=' ')
    print()


# range(start, stop, increment/decrement)