## 큰수의 법칙
**기출**: 2019 국가 교육기관 코딩 테스트   
**난이도** ★☆☆
* * *

### 문제

다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
예를 들어 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자. 이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다.

단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자. 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 4 + 4 + 4 + 4 + 4 + 4 + 4인 28이 도출된다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

* * *


### 입력 조건
- 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 이루어진다
- 입력으로 주어지는 K는 M보다 항상 작거나 같다

### 출력조건
- 첫째 줄에 큰수의 법칙에 따라 더해진 답을 출력한다.

### 입력예시
```
5 8 3
2 4 5 4 6
```

### 출력예시
```
46
```
* * *
## 해설 1
M번 더해서 최댓값이 나와야하고 같은 수는 K번 넘게 반복될 수 없다는 문제다.
그리디하게 생각해보면 배열에서 '**가장 큰 수**'와 '**두번째로 큰 수**'를 찾은 후 "**가장 큰 수를 K번 더하고 두번째로 큰 수를 한번 더하는 연산**"을 반복하면 된다! 이를 바탕으로 소스코드를 작성해보자

## 소스코드 1
```python
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
```
하지만 이 코드는 숫자를 모두 하나하나씩 반복문을 통해 더해주기 때문에 시간복잡도 측면에서 약하다. 만약 M의 크기가 100억 이상처럼 커진다면 시간초과 판정을 받을 것이다. 규칙성을 파악하여 더 효율적으로 문제를 해결해보자.

## 해설 2
지금 수열 6, 6, 6, 5가 반복되고 있는 상황이다. 반복되는 수열의 길이는 얼마일까? (K + 1) 이다. 따라서 수열이 반복되는 횟수는 M // (K+1)이 된다.
M이 K+1로 나누어떨어지지 않는다면 그 나머지 만큼 first를 더하면 된다.

## 소스코드 2
```python
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
```


