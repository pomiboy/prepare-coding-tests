N = int(input()) # 테스트케이스 수 정수로 입력받기

area = 1 # 초기 area값 설정
for _ in range(N):
    h, w = map(int, input().split()) # h, w 입력받기
    area = h * w if h*w > area else area # 원래 area와 비교하여 h*w값이 더 크다면 area에 새로 할당
    # 반복문이 다 돌면 area에는 h*w 값 중 가장 큰 값이 할당되어있을 것임

print(area) # area 출력