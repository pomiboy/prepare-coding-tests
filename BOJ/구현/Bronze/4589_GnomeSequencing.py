N = int(input()) # 테스트케이스 수 N 정수로 입력받기

print("Gnomes:")

for _ in range(N):
    length_list = list(map(int, input().split())) # 수염길이 배열로 입력받기
    # 입력받은 수염길이배열이 오름차순이거나 내림차순이면 "Ordered" 출력
    if length_list == sorted(length_list) or length_list == sorted(length_list, reverse=True):
        print("Ordered")
    else: # 아니면 "Unordered 출력"
        print("Unordered")