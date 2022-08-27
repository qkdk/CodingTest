s = input()
sum = 0
char = []

numbers = [str(x) for x in range(10)]

for i in s:
    if i in numbers:
        sum += int(i)
    else:
        char.append(i)

char.sort()
print(''.join(char) + str(sum))
