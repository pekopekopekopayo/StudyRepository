# 로마 문자의수 값은 밑과 같다.
# 'I': 1
# 'V': 5
# 'X': 10
# 'L': 50
# 'C': 100
# 'D': 500
# 'M': 1000
# 로마 문자의 수는 항상 왼쪽이 크고 오른쪽이 작다.
# 로마 문자의 수가 만약 왼쪽이 작다면 그것은 하나 의 수로 생각을 한다.
# ex IV 일 경우에는 5 - 1 4가 되는 것 이다.
# 입력 값으로 로마 문자의 수가 입력되었을때 로마의 수의 합계를 10진수로 구하여라  

class Solution:
        
    def romanToInt(self, s: str) -> int:
        dic = {
                'None': 0,
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
                }
        result = 0
        s = list(s)
        while s:
            s1 = s.pop()
            if s: s2 = s.pop()
            else: s2 = 'None'
            
            if dic[s1] <= dic[s2]:
                result += dic[s1]
                s.append(s2)
            else:
                result += dic[s1] - dic[s2]
        return result