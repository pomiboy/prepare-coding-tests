# N, K 공백을 구분하여 입력받기
N, K = map(int, input().split())

count = 0 # 수행 횟수
while True:
    if N % K == 0: # N이 K로 나누어 떨어지면 K로 나누기 (2번 수행)
        N //= K
        count += 1
    else:
        N -= 1 # 나누어 떨어지지 않는다면 1을 빼기(1번 수행)
        count += 1
    
    if N == 1: # N이 1이되면 반복문 탈출
        break

print(count) # 최종 횟수 출력