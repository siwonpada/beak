def binToG(b: int) -> int:
  str_b = format(b, 'b')
  list_b = list(str_b)
  list_b.pop(0)
  list_G = [4 if i == '0' else 7 for i in list_b]
  return int(''.join(map(str, list_G)))

N, M = map(int, input().split())

G_NUM = [4, 7]
G = int('0b1' + '0' * len(str(N)), 2)

while binToG(G) < N:
  G += 1

res = 0
while binToG(G) <= M:
  res += 1
  G += 1

print(res)