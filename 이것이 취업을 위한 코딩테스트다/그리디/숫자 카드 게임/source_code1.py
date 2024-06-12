# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split()) 

cards = [] # 카드들을 담은 배열 생성
# 행 별로 입력받아 card 배열 안에 넣어주기
for i in range(N):
    cards.append(list(map(int, input().split())))

# 각 행을 반복문으로 돌며 행의 최솟값 중 최댓값을 result에 할당하기
for i in range(N-1):
    result = min(cards[i]) if min(cards[i]) >= min(cards[i+1]) else min(cards[i+1])

print(result)
