#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
#N개의 자연수 입력받아 배열로 만들어주기
num_list = list(map(int, input().split()))

#오름차순 정렬하기
num_list.sort()

#가장 큰 수와 두번째로 큰 수 찾기
first = num_list[-1]
second = num_list[-2]

# 수열의 합
num_sum = (first * k) + second

# 규칙에 맞게 최대합 구하기
result = num_sum * (m // (k+1)) + first * (m % (k+1))

print(result)