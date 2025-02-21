N = int(input())
arr = [(i, True) for i in range(N+1)]
for i in range(1, N+1):
  parentId = int(input())
  while not arr[parentId][1]:
    parentId = arr[parentId][0]
  arr[i] = (parentId, False)
  if parentId == i:
    arr[i] = (i, True)

for i in range(1, N+1):
  parentId = arr[i][0]
  if arr[i][1]:
    continue
  while not arr[parentId][1]:
    parentId = arr[parentId][0]
  arr[i] = (parentId, False)
  
res = 0
for i in range(1,N+1):
  if arr[i][0] == 0:
    res += 1

print(res)
