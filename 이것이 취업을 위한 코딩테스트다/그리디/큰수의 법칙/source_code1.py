#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#N개의 자연수 입력받아 배열로 만들어주기
num_list = list(map(int, input().split()))

#오름차순 정렬하기
num_list.sort()

#가장 큰 수와 두번째로 큰 수 찾기
first = num_list[-1]
second = num_list[-2]

sum = 0

while True:
    for i in range(k): # 가장 큰수 K번 더하기
        sum += first
        m -= 1 # 한번 더할떄마다 M 1씩 줄이기
        if m == 0: # M이 0 되면 break
          break
    sum += second # 두번째 큰수 한 번 더하기
    m -= 1
    if m == 0:
      break

print(sum) # 최종답안 출력