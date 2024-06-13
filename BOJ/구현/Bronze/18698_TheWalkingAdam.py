N = int(input()) # 테스트케이스 수 N 정수로 입력받기

for _ in range(N):
    walks = input() # 걸음걸이 문자열로 입력받기
    if 'D' in walks:
        # 'D'가 문자열에 포함된 경우 'D' 전까지의 문자열의 길이 구하기
        steps = len(walks[:walks.index('D')])
        print(steps)
    else: # 'D'가 없는 경우 전체 문자열의 길이 출력
        print(len(walks))