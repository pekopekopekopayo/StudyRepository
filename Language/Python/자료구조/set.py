# set은 데이터의 집합이다.
# set의 특징은 데이터의 집합이며 중복과 순서가 없다.
# 또한 합 교 차 집합 연산도 가능하다.
# set은 인덱스 접근이 불가하다.

# set은 밑과 같이 선언 가능하다.
my_list = set([1,2,3,4,5,6,7,1,1,1,1,1])
print(my_list)
# 데이터를 추가 할 경우는 밑과 같이 사용한다.
my_list = set()
my_list.add(2)
my_list.add(1)
my_list.add(1)
my_list.add(3)
my_list.add(2)
print(my_list)
# 삭제도 가능하다. 2라는 데이터가 삭제된다.
my_list.remove(2)
print(my_list)


# 합 교 차 집합은 아래와 같이 사용가능하다. 
print(set([1,2,3]) | set([3,4,5,6]))
print(set([1,2,3]) & set([3,4,5,6]))
print(set([1,2,3]) - set([3,4,5,6]))

# 문제 
# peko와 pepe는 좋아하는 취미를 이야기를 하고 있다.
# peko와 pepe는 말하는 것을 너무 좋아하여 똑같은 이야기를 반복 할 때도 있다.
# peko와 pepe는 n만큼 이야기를 한다. 이때 peko와 pepe의 같은 취미는 무엇인가 출력하라.
# !출력은 오름차순으로 출력한다.
# !항상 peko가 처음으로 이야기를 하고 두번째로 pepe가 이야기를 한다.
# input
# 6
# 배드민턴 테니스
# 테니스 배드민턴
# 수영 아이돌
# 유튜브 넷플릭스
# 애니메이션 드라마
# 헬스 헬스

s1 = set()
s2 = set()
for i in range(6):
  one, two = input().split()
  s1.add(one)
  s2.add(two)

print(sorted(list(s1&s2)))