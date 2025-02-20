N, M = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
dp_arr = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
  for j in range(M):
    if i == 0 and j == 0:
      dp_arr[i][j] = map_arr[i][j]
    elif i == 0:
      dp_arr[i][j] = dp_arr[i][j-1] + map_arr[i][j]
    elif j == 0:
      dp_arr[i][j] = dp_arr[i-1][j] + map_arr[i][j]
    else:
      dp_arr[i][j] = max(dp_arr[i-1][j], dp_arr[i][j-1], dp_arr[i-1][j-1]) + map_arr[i][j]

print(dp_arr[N-1][M-1])