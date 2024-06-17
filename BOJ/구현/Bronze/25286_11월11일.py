N = int(input()) # 테스트케이스 수 N 정수로 입력받기

# 윤년인지 구해주는 함수
def is_leap_year(x):
    if x % 400 == 0:
        return True
    elif x % 4 == 0 and x % 100 != 0:
        return True
    return False

for _ in range(N):
  year, m = map(int, input().split()) 

  if m == 1:
      month = 12
      date = 31
      year -= 1
  else:
      month = m - 1
      if m in [5, 7, 10, 12]:
          date = 30
      elif m in [2, 4, 6, 8, 9, 11]:
          date = 31
      elif m == 3:
          date = 29 if is_leap_year(year) else 28

  print(year, month, date)