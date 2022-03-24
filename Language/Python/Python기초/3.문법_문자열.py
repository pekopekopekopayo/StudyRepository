# 파이썬은 쉽게 문자열을 사용 할 수 있다.
string = 'yello world'
# string[0] = 'h' # 파이썬의 문자열 고정 값을 가지고 있으므로 수정 할 수 없다. 
string = 'hello world' # 재할당을 받는 것은 가능하다.
print(string)

# 파이썬에서는 문자열에 곱하기 더하기 곱하기 연산이 가능하다.

# 더하기는 문자열을 덧붙이는 기능을 한다.
print("hello" + " world")

# 곱하기는 문자열을 곱한 수만큼 복사한다.
print('hello world ' * 2)

# print를 사용할때 줄 바꿈을 원치 않는다면 밑과 같이 사용한다.
print('hello', end='')
print(' world')

# 숫자를 문자열로 변환 시키려면 str()을 사용하여 문자로 치환 시킬 수 있다.
print(str(11))

string = 'world'
# 문자열에 변수를 넣을 수 있는 기능도 존재한다.
print(f"hello {string} {1} {2} {3}") # 이때는 f''작은 따옴표가 아닌 f""큰 따옴표를 사용해야한다. 그리고 변수는 꼭 {}안에 입력 해야한다. 