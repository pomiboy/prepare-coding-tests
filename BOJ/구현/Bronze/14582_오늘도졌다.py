woolim = list(map(int, input().split()))
gulivers = list(map(int, input().split()))

sum_w = 0
sum_g = 0
for i in range(9):
    sum_w += woolim[i]
    if sum_w > sum_g: # 한번이라도 울림이 걸리버스를 이기고 있는 순간이 있다면 바로 break
        print("Yes")
        break
    sum_g += gulivers[i]
    if i == 8:
        print("No")