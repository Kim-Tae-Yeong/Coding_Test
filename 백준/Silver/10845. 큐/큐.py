from collections import deque as d
import sys

n = int(input())
q = d([])
for _ in range(n):
  command = list(map(str, sys.stdin.readline().strip().split()))
  if(command[0] == 'push'):
    q.append(int(command[1]))
  elif(command[0] == 'pop'):
    if(len(q) == 0):
      print(-1)
    else:
      print(q.popleft())
  elif(command[0] == 'size'):
    print(len(q))
  elif(command[0] == 'empty'):
    if(len(q) == 0):
      print(1)
    else:
      print(0)
  elif(command[0] == 'front'):
    if(len(q) == 0):
      print(-1)
    else:
      print(q[0])
  elif(command[0] == 'back'):
    if(len(q) == 0):
      print(-1)
    else:
      print(q[-1])