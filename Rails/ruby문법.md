# map each
> result = [1,2,3].map { |n| n * 2}   
> result == [2,4,6]   
> result = [1,2,3].each { |n| n * 2}    
> result == [1,2,3]   
> map은 반환 값으로 `변경된 값`을 반환한다.   
> each는 반환 값으로 `원래 값`을 반환한다.    
      
# first
> 배열 또는 리스트 형식의 첫번째 값을 반환한다.   
> [2,1,3,5,7].first == 2    
     
# nil?    
> `루비 함수의?는 return 값이 boolean을 뜻한다`   
> nil?은 현재 값이 nil인지 확인한다. 맞을 경우 True 틀릴 경우 False를 반환한다.   
> nil.nil? == True      
> 1.nil? == False   
     
# empty?
> array hash set String과 같은 리스트 형식의 객체가 비어있을때 True 요소가 존재한다면 False를 반환한다.   
> [].empty? == True   
> [1,2,3].empty? == False   
> '' == True    
> "peko" == False   
     
# blank?
> nil? 성질과 empty? 성질이 합쳐져있다.   
> nil 또는 비워져있는 array hash set 문자열에 대해서 True 값을 반환 한다.   
> 또한 " "같은 공백도 비어있다고 판단한다.    
> "".blank? == True   
> " ".blank? == True    
> nil.blank? == True    
      
# present?
> blank?의 정반대이다.    
> 식은 생략하겠다. 비워져있는 것들에 대해서는 False를 반환한다고 생각하자.    

# inject
> [1,2,3,4,5].inject {|s(합계변수 초기값 0), o(배열의 요소)| s += o} => 15
> [1,2,3,4,5].inject(500) {|s(합계변수 초기값 500), o(배열의 요소)| s += o} => 515
> 배열의 계산기 기능을 담당한다. 최종적으로 합계 변수의 값을 반환한다.

# reject
> [1,2,3,4,5].reject {|o| o >= 3} => [1, 2]
> reject는 반환값이 `true인 요소를 제외`하고 배열을 반환한다.

# %i %w
> %i['hello my name is peko'] => [:"'hello", :my, :name, :is, :"peko'"]
> 공백을 기준으로 단어들을 `심볼 값`의 배열로 치환 해준다..
> %w['hello my name is peko'] => ["'hello", "my", "name", "is", "peko'"]
> 공백을 기준으로 단어들을 `문자열`의 배열로 치환 해준다.

# count
> DB에서 카운터를 사용하여 몇개의 레코드를 검색하였는지 결과 값을 반환함

# length
> 배열의 길이를 반환함
