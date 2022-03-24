# C

```
#include <stdio.h>

int main()
{
    int numbers[10] = { 1,2,3,4,5,6,7,8,9,10 };

    for (int i = 0; i < sizeof(numbers); i++)
    {
        printf("%d\n", numArr[i]);
    }

}
```
# Python
```
numbers = [1,2,3,4,5,6,7,8,9,10]
for n in number: print(n)
print(numbers)
```

**파이썬은 동적언어이기 때문에 자료형 지정이 필요없습니다.**
**파이썬에서는 세미클론을 찍으시면 안됩니다.**
**배열도 크기도 동적이기 때문에 배열 크기도 할당 안하고 사용 할 수 있다. print함수에서 배열도 바로 출력이 가능하다.**