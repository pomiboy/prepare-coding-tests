h = int(input()) # 구멍의 개수 정수로 입력받기

number = ''

# 구멍 개수 0일때와 1개일때는 특수 경우이므로 따로 먼저 처리 해줌
if h == 0:
    number += '1'
elif h == 1:
    number += '0'
else: # 구멍 개수 2개 이상인 경우
  while True:
      if h % 2: # 구멍 개수가 홀수인 경우
          number += '4' # 구멍이 하나인 수 중 가장 작은 수인 4 넣어줌으로써 구멍 하나 clear
          h -= 1 # 하나 clear 했으니 남은 구멍 개수 하나 뺴줌
      else: # 구멍 개수가 짝수인 경우
          number += '8' # 숫자 하나로 구멍 2개를 clear할 수 있어버리는 8 넣어줌
          h -= 2
      if h == 0: # 구멍개수 모두 clear하면 break
          break

print(number) # 최종값 출력