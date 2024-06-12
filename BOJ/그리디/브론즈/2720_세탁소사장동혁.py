T = int(input()) # 테스트케이스 수 정수로 입력받기

for _ in range(T):
    change = int(input()) # 거스름돈 입력 받기

    quarter = change // 25 # 쿼터 개수 구하기
    change -= 25 * quarter # 쿼터를 사용해 거슬러 준 만큼 빼기

    dime = change // 10 # 남은 금액에서 거슬러 줄 수 있는 dime 개수 구하기
    change -= 10 * dime # dime을 사용해 거슬러 준 만큼 빼기

    nickel = change // 5 # 남은 금액에서 거슬러 줄 수 있는 nickel 개수 구하기
    change -= 5 * nickel # nickel을 사용해 거슬러 준 만큼 빼기

    penny = change // 1

    print(quarter, dime, nickel, penny)