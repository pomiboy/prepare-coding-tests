N = int(input()) # 셀의크기 정수로 입력받기

# 세로축 구현
for _ in range(4):
    for _ in range(N):
      print("@" * N)

# 가로축 구현
for _ in range(N):
    print("@"*(5*N))