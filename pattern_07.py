n = int(input('Enter the value of n:'))
temp = 0
for row in range(1, n+1):
    for col in range(1, n+1-temp):
        print(n, '', end='')
    temp = temp + 1
    print()
