4부터 입력받은 수까지 dp 실행

  - i가 6으로 나눠지면 (i - 1), (i // 3), (i // 2)의 경우 중 가장 작은 횟수에 1 더함
  - i가 3으로 나눠지면 (i - 1), (i // 3)의 경우 중 가장 작은 횟수에 1 더함
  - i가 2로 나눠지면 (i - 1), (i // 2)의 경우 중 가장 작은 횟수에 1 더함
  - 그 외의 경우 (i - 1)의 경우에 1 더함
