N = int(input())

# 브루트 포스 -> 그냥 냅다 1부터 전수조사!!
for i in range(1, N+1):
    # 자릿수 합 구하기
    sum = 0
    for num in str(i):
        sum += int(num)
    # 분해합 구하기
    total_sum = i + sum

    # 분해합이 N과 같으면 생성자 i 출력
    if total_sum == N:
        print(i)
        break
    if i == N: # 분해합이 N이 되는 i가 없었다는 뜻
        print(0)