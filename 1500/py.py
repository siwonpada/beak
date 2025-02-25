S, K = map(int, input().split())

arr = []
for i in range(K, 0, -1):
  arr.append(S // i)
  S -= S // i

res = 1
for i in arr:
  res *= i

print(res)