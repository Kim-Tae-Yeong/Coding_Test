n, k = map(int, input().split())
board = []

for _ in range(n):
  country = list(map(int, input().split()))
  board.append(country)

board.sort(key = lambda x : (-x[1], -x[2], -x[3]))

ans = 0
cnt = 1
tmp = []
for i in range(n):
  if(tmp == board[i][1:]):
    cnt += 1
  else:
    tmp = board[i][1:]
    ans += cnt
    cnt = 1
  if(board[i][0] == k):
    print(ans)
    break