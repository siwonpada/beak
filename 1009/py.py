N = int(input())
for _ in range(N):
  a, b = map(int, input().split())
  res = 1
  for _ in range(b):
    res = (res * a) % 10
  print(res if res != 0 else 10)
  