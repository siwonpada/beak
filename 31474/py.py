N = int(input())
res = 1
for i in range(1, N+1):
  res *= i
  if res % 2 == 0:
    res //= i
print(res)