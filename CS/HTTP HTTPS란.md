# HTTP
> HTTP란 `Hyper text transfer protocol`이다.    
> 인터넷에서 주로 문자 데이터를 주고 받는 프로토콜이다.     
> HTTP는 TCP/IP 프로토콜 위에서 작동하며 웹 서버와의 통신에 사용된다.(웹용 프로토콜이라고 생각해도 무방하다.)    
> HTTP는 크게 Header 와 Body로 나누어진다. 그리고 모든 값들은 key: value 형식이다.     
> 많은 요소를 가지고 있기 때문에 간단히만 설명하겠다.    
> 요청 Header은 URL과 Method(GET, POST, PATCH, PUT, DELETE `요청 생성 수정 일부수정 삭제`)등을 가지고 요청을 보낸다.    
> 응답 Header은 요청한 값의 응답 그리고 응답에 대한 정보를 전달 한다.     
> 요청 Body는 HTML Form Input에 대한 입력 값이 들어간다. 이때 형식은 `Post`이여야 한다. 만약 서버에게 주고 싶은 정보가 없다면 공백 처리가 된다.     
> 응답 Body 또한 돌려줄 값이 존재한다면 클라이언트에게 돌려 줄 수있다. 물론 정보가 없다면 공백 처리다.     
> 흐름은 아래와 같다.    
>
> 1. 클라이언트(브라우저)가 Google.com에 접속하고 싶다. 그러니 Google서버에게 Google.com이라는 자료 요청(GET)을 해보자    
> 2. 서버는 우리가 읽을 수 있는 문자로 되어 있지만 사실 실제 주소는 숫자로 되어 있다.(IP) 그러므로 `DNS서버`에서 우리는 Google.com에 대한 아이피 주소를 알아온다.    
> 3. 구글의 IP주소를 알아냈으니 Google 서버와 TCP/IP를 거치고 서로 3-Way-HandShake을 거친다.    
> 4. 그럼 서버가 GET Google.com 이라는 것을 받을 것 이다. 서버는 Get이란 형식으로 Google.com의 요청이 왔기 때문에 자료요청이라고 알 수 있다.    
> 5. 서버는 Google.com의 정보를 클라이언트에게 전달을 하고 4-Way-HandShake를 한 뒤 `연결종료`한다.    

# HTTPS
> HTTPS란 HTTP의 특성을 가지고 있으며 보안을 강화한 버전이다.    
> HTTP 프로토콜은 사람이 읽을 수 있게 설계가 되어있다.    
> 만약에 제3자가 HTTP프로토콜을 탈취를 하면 정보 유출에 대한 위험성이 크다.    
> HTTP 프로토콜의 암호화 버전이 HTTPS가 되는 것이다.     
> HTTPS는 암호화 버전이기 때문에 HTTP와 엄청난 변화는 없다.     
> HTTPS가 되는 방법은 밑과 같다.    
> 1. 서버 운영자는 자기 서버가 무슨 어떤 서버인지 정리 하여 글을 쓴다.           
> 2. 서버의 개인키와 그 개인키의 공개키를 만든다.      
> 3. 그리고 서버 설명과 공개키를 인증기관에 제출한다.(요금 발생)     
> 4. 인증기관에서 문제 될게 없으면 인증 기관의 개인키 와 제출한 정보를 이용해 암호화 인증서를 만들어 제공 한다.     
> 5. 인증기관은 웹 브라우저에게 자기의 공개키를 공개한다.(브라우저를 다운받을때 인증기관의 공개키도 같이 다운 됩니다.)     
> 6. 클라이언트가 서버로 요청을 보낼때 요청된 응답과 서버 인증서를 보낸다.      
> 7. 클라이언트(브라우저)에는 인증기관의 공개키가 있으니 그 인증기관의 공개키로 인증서를 복호화 시킨다. 그러면 인증서에서 사이트의 정보와 서버의 공개키를 알 수 있다.     
> 8. 그 공개키를 이용하여 대칭키를 암호화 시켜 생성한다. 그리고 그것을 서버에다 넘겨준다.      
> 9. 서버는 개인키로 암호화 된 대칭키를 해독한다 그렇게 되면 서버는 대칭키를 얻게 되는 것이다.      
> 10. 이 두 대칭키를 가지고 송수신을 할때 내용을 대칭키를 사용해서 암호화를 한다. 대칭키는 서로 서로가 들고 있으니 복호화가 가능하다.    