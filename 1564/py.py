def reduce0(N : int) -> int:
  s_res = str(N)
  while len(s_res) > 1:
    if s_res[-1] == '0':
      s_res = s_res[:-1]
    else:
      break
  return int(s_res)

N = int(input())

res = 1
for i in range(1, N+1):
  res *= i
  res = reduce0(res) % 10**12

print(str(res % 100000).zfill(5))