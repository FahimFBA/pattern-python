n = int(input('Enter the value for n: '))
temp = 0
for row in range(n, 0, -1):
    temp = temp + 1
    for col in range(1, row+1):
        print(temp, '', end='')
    print()
