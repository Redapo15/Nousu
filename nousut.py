num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
nou1 = 0
nou2 = 0
x = 0
print(len(num1))
while x < len(num1):
    
    if num1[x] != 0 and x == 0:
        nou1 += num1[x]
    elif num1[x - 1] < num1[x]:
        nou1 += (num1[x] - num1[x - 1])

    if num2[x] != 0 and x == 0:
        nou2 += num2[x]
    elif num2[x - 1] < num2[x]:
        nou2 += (num2[x] - num2[x - 1])
    
    x += 1


print(num1)
print(nou1)
print(nou2)