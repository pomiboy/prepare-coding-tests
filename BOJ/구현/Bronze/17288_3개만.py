numbers = input()

count = 0
real_count = 0

for i in range(1, len(numbers)):
    if int(numbers[i]) - int(numbers[i-1]) == 1:
        count += 1
    else:
        if count == 2:
            real_count += 1
        count = 0
    if i == len(numbers) - 1 and count == 2:
        real_count += 1

print(real_count)
        
    