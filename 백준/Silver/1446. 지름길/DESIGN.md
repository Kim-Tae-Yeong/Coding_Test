입력받은 지름길 중 조건에 맞는 지름길만 배열에 추가

  - 지름길의 도착 지점 값이 원래 도착 지점 값보다 작음
  - 지름길을 이용하는게 더 이득임( = 지름길의 길이가 도착 지점 값에서 시작 지점 값을 뺀 길이보다 작음)

도착 지점까지의 배열 선언

이후 길이를 1씩 늘리면서 dp로 탐색

  - 도착 지점이 i인 곳의 길이는 i와 (i - 1)에서 1 더한 값 중 작은 값으로 설정
  - i가 지름길의 시작 지점이고, (i까지의 길이 + 지름길의 길이)가 지름길의 도착 지점의 길이보다 작으면 도착 지점의 값을 해당 값으로 바꿈
