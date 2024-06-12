# M, H 공백 구분하여 정수로 입력받기
M, H = map(int, input().split())

# N 정수로 입력받기
N = int(input())

happiness = 0 # 시작 행복도 설정

# N번 반복하며 더 큰 행복도를 주는 값을 happiness에 더함
for _ in range(N):
    c, b = map(int, input().split())
    happiness += M * c if M * c >= H * b else H * b

print(happiness) # 최종 행복도 출력