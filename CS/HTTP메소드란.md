# HTTP메소드
> HTTP 프로토콜에는 메소드가 존재한다. `중요한 내용`이지만 간단한 내용이기 때문에 쉽게 설명을 하겠다.    

# GET
> GET 메소드는 URL에 자원을 요청하는 메소드이다.    
> 클라이언트는 이런 자원을 URL에 표시한다. 예시로 `peko.com/animal?type=강아지` 를 서버에 GET방식으로 서버에게 전달해보자.    
> 이때 자원은 `type=강아지` 이다. 그리고 자원은 HTTP의 HEAD에 저장된다.    
> 위에 내용을 토대로 해석을 하면 `peko.com/animal`이라는 페이지에 `type=강아지` 라는 것을 요청을 하는 것이다.     
> 쉽게 `?` 뒤에는 요청 값이 있다고 생각하면 된다. `?`가 없다면 요청 값은 없고 페이지만 보여달라는 뜻이다.    
> 만약 요청이 두개 이상일 경우는 `peko.com/animal?type=강아지&sex=남자` &을 붙이면 된다.     
> 만약 `peko.com/animal`은 동물 사진 게시판이다. URL에 `peko.com/animal?type=강아지` 를 서버에 요청하게 된다면  서버에서는 강아지의 사진만 골라서 웹 페이지에 보여줄 것이다.    
> 브라우저는 GET방식으로 무언가를 요청하고 응답을 받았을때 그 응답을 `캐싱`(임시 저장)을 한다. 똑같은 요청을 계속 하면 응답이 느려지기 때문이다.    
> 

# POST
> POST는 등록하는 메소드이다.     
> `peko.com/animal/create`는 게시물을 작성 할 수 있는 페이지이다.    
> 이 페이지에서 게시물을 작성을 하면 HTTP의`Body`에 게시물 내용이 들어가게 된다. `POST방식은 URL에 자원을 표시하지 않는다.`    
> 서버는`POST`방식으로 요청을 받았다면 Body를 살펴 볼 것이다. 그리고 그 내용을 기반으로 데이터를 저장한다.    


# GET과 POST 차이점
> 쉽게 GET방식은 URL에 자원이 표시가 되고 POST는 URL에 자원이 표시가 되지않는다.    
> 위와 같이 `GET 방식은 URL에 자원이 표시가 됨으로 보안성이 낮고 POST는 URL에 자원이 표시가 되지 않기 때문에 보안성이 GET방식 보다는 높다.`    
> `그럼 POST방법만 쓰면 되는거 아닌가요?` 라고 질문을 했을때 POST방식만 사용하게된다면 `peko.com/animal?type=강아지` 이런 페이지를 요청 할 수 없습니다.    

# PUT
> PUT는 한 데이터의 요소를 모두 갱신 할 때 사용한다.     
> POST 요청 방식은 같다. 틀린점은 `멱등성`이라는 개념이다. 물론 한국인이지만 멱등성이라는건 나도 처음 들어봤다ㅋㅋ;;    
> `멱등성`이라는 개념은 `연산을 여러번 해도 본질은 달리지지 않는 성질`이라는 뜻 이다. 이것에 대해서는 나도 정보를 많이 찾아봤지만 이해가 잘 가지 않는다.     
> `PUT과정은 POST도 할 수 있다.` 하지만 Role을 지키자 PUT 한 데이터의 요소를 모두 갱신 할 때 사용하자 (만약 추후 멱등성이라는 것이 이해가 되어 설명 할 수준이 되면 글을 수정 하겠다.)    

# PATCH
> PATCH는 한 데이터의 일부 요소를 갱신 할 때 사용한다.    
> 또한 POST 요청 방식과 같다.    
> 하지만 일부 요소를 갱신 할 때에는 PATCH를 사용하는 약속을 지키자.    

# DELETE
> DELETE는 한 데이터를 삭제 할 때 사용한다.    
> 또한 POST 요청 방식과 같다.   


# PUT PATCH DLETE는 요청방식은 POST와 같나요?
> 반대로 GET방식처럼 해보자 그러면 클라이언트는 갱신 삭제요청을 URL로 할 수 있다. 바로 감이 오실거라고 생각한다.