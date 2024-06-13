import math

N = int(input()) # 참가자 수 정수로 입력받기
tshirt_numbers = list(map(int, input().split()))
T, P = map(int, input().split())

# 티셔츠를 T장 씩 최소 몇 묶음 주문해야 하는지 출력
sum = 0 # 초기값 설정
for tshirt in tshirt_numbers:
    sum += math.ceil(tshirt / T)
print(sum)

# P자루씩 최대 묶음 -> 몫, 한자루씩 몇개 -> 나머지
print(N // P, N % P)