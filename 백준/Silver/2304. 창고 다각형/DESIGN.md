입력받은 값에서 시작 x와 끝 x, 최대 높이와 그에 해당하는 x를 저장

가장 먼저 시작 지점부터 최대 높이 지점까지의 면적을 구함

  - 시작 지점의 높이를 변수로 설정
  - 이후 높이가 변수보다 크면 변수를 해당 높이로 바꿈

그 다음으로는 최대 높이 지점부터 마지막 지점까지 면적을 구함

  - 최대 높이 지점이 마지막 지점과 같으면 위 과정을 할 필요가 없음
  - 새로운 배열을 만들어 i번째 요소에 i번째부터 마지막 지점까지의 높이 중 가장 높은 값을 저장
