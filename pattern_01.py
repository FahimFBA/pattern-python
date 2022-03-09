n = int(input('Enter the number of rows: '))
for row in range(n + 1):
    for col in range(row):
        print('* ', end = "")
    print()