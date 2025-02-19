N = int(input())
M = input()
K = int(input())
flag = True
if N-K < 0:
  for i in range(N):
    if M[i] != '0':
      flag = False
      break
else:
  for i in range(N-K, N):
    if M[i] != '0':
      flag = False
      break
print('YES' if flag else 'NO')