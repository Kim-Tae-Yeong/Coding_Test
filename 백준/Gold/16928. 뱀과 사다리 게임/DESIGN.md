1에서 시작 -> 2 ~ 7까지는 1번에 갈 수 있음

  - [2, 1], [3, 1], ..., [7, 1]을 큐에 넣음

이후 큐에서 원소를 하나씩 빼면서 해당 위치에 사다리 or 뱀이 있는지 확인

  - 사다리 or 뱀이 존재하면 타고 이동
    - 이때 가는 횟수는 변하지 않음
  - 없으면 해당 위치부터 + 1, + 2, + 3, ..., + 6 위치까지 이동
    - 이때 가는 횟수는 (이전 횟수 + 1)
