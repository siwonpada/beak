N = int(input())
arr = list(map(int, input().split()))
stack = []
for i in range(N):
  if len(stack) == 0:
    stack.append(arr[i])
  elif (stack[-1] + arr[i]) % 2 == 0:
    stack.pop()
  else:
    stack.append(arr[i])
print(len(stack))