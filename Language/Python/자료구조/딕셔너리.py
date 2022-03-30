# dictionary 선언법

# key와 value로 선언한다.
from collections import defaultdict
from email.policy import default


dic = {'key': 'value'}
dic = dict({'key': 'vlaue'})
print(dic['key'])
# 유효하지 않는 key는 에러를 발생시킨다.
# print(dic['peko'])

i_like = {'apple': 'yes', 'pair': 'no', 'orange': 'yes'}

# 모든키를 알고 싶을 경우에는 아래와 같이 출력 가능하다.
print(i_like.keys())


# 문제

# peko는 나쁜사람이다. peko는 포켓몬 빵 사재기를 하려고 한다.
# peko는 n번만큼 편의점 또는 마트를 방문 할 수있다.
# 모든 편의점 마트를 둘러다니면서 포켓몬 빵을 모두 사간다.
# n번만큼 편의점 마트를 방문했을때 peko는 무슨빵을 몇개 가지고있는지 출력하라
# 출력시 빵의 이름 순서대로 정렬 한뒤 갯수를 출력하라
# 만약 마트 편의점에 포켓몬빵이 없을 경우 `없음 0`이 입력이 된다. 그럼 peko는 편의점 마트를 떠날 것 이다.

# input
# 3
# 없음 0
# 고스트빵 2
# 피카츄빵 2
# 없음 0
# 파이리빵 1
# 로켓단빵 3
# 고스트빵 2
# 없음 0

# output
# 고스트빵: 4개 가지고 있습니다.
# 피카츄빵: 2개 가지고 있습니다.
# 파이리빵: 1개 가지고 있습니다.
# 로켓단빵: 3개 가지고 있습니다.

n = 3
dic = {}
for i in range(n):
  while True:
    key, value = input().split()
    if key == '없음': break
    if key in dic: dic[key] += int(value)
    else: dic[key] = int(value)

for key in dic.keys():
  print(f"{key}: {dic[key]}개 가지고 있습니다.")