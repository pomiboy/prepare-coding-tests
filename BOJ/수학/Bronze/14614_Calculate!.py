a, b, c = map(int, input().split())

# XOR 연산은 두번하면 자기 자신이기 때문에 C%2번만큼 연산해주어도 괜찮다
# 이렇게 하지 않으면 문제에서 시간초과가 난다
for _ in range(c%2):
    a ^= b

print(a)