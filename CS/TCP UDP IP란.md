# IP
> IP는 `네크워크 계층 프로토콜` 이다.   
> IP는 송 수신처에 대한 이 있다.  그리고 라우팅을 하는 프로토콜이다.   
> IP는 패킷을 전송하는 역활도 할 수 있다. 하지만 전송 제어가 되지 않는다.

# TCP
> TCP란 `전송 계층 프토토콜` 이다.   
> IP위에서 동작하니 송신이 가능하다. TCP는 수신 또한 가능하다. 이때 `3handshake` `4handshake`라는 과정을 거친다. `이 과정을 설명하면 본문이 길어짐으로 추후 따로 설명하겠다.`   
>    
> TCP는 패킷을 교환 하는 방식을 사용한다. 하나의 회선에 모든 패킷을 넣다보면 그 회선에 문제가 발생시 모든 패킷이 누락이 될 수 있다.   
> 이러한 문제점이 발생이 되니 여러가지의 회선에서 회선으로 패킷을 교환하여 마지막은 수신측으로 간다. 이렇게 하면 누락은 일어 날 수 있지만 모든 패킷이 누락되진 않는다.   
> 이러하듯 `누락은 발생 할 수 있다.` 하지만 누락이 된 패킷은 있어서는 안될때가 있다. 그러므로 TCP는 패킷의 순서를 정하고 차례대로 패킷을 전송을 한다.   
> 그러면 수신측에서도 차례대로 패킷이 올 것이고 그 패킷 중에 순번이 있으니 분실 또는 파손 된 패킷을 알 수 있고 재 요청을 할 수 있을 것 이다.   
> 하지만 패킷이 만약에 크다면 재 요청 송신도 부담이 된다. 그렇기 때문에 TCP는 패킷을 잘게 잘라서 순서대로 보내는 형식을 취한다.   
> 패킷이 순서대로 도착했으면 모든 패킷을 조립(순번)하여 데이터가 올바르게 전송 된다.   
> 위와 같은 방법이라면 데이터 누락 없는 송 수신이 이루어 질 것 이다.   
>     
> `TCP는 최강은 아니다.` 위의 방법을 읽어보면 읽기도 힘들고 이해하기도 힘들 수도 있다. 그것을 처리하는 컴퓨터(CPU)는 얼마나 힘들겠는가. 그러므로 TCP는 `전송 속도가 낮고 신뢰성은 크다`.   

# UDP
> UDP란 `전송 계층 프로토콜` 이다.   
> UDP도 똑같이 패킷 교환 방식을 사용한다.    
> 크게 보았을때 UDP는 TCP에 비해 간단한 움직임을 한다.    
> UDP는 IP위에 동작한다. 그러니 송신이 가능하다. 하지만 수신은 할 수 없다.    
> 그러니 `누락은 발생 할 수 있지만` TCP보다 제약이 없기 때문에 `전송 속도는 빠르다` 그리고 `신뢰성이 낮다`.   
> UDP는 자기만의 독단적인 `패킷(데이터그램)`을 사용한다. 이 패킷의 데이터의 그릇이 크다. 즉 데이터가 크게 담길수 있다는 뜻 이다.   
> 재 요청이 안되고 패킷 분실해도 괜찮으니깐 큰 패킷 큰 패킷 이런식으로 전송을 한다.    


# TCP UDP 예시
> 만약에 다운로드를 한다고 과정하자. `실제로는 FTP프로토콜 사용 TCP/IP위에서 동작`    
> TCP방식으로 한다면 시간은 걸릴수도 있지만 완벽한 파일을 다운로드 할 수 있을 것 이다.   
> UDP방식으로 한다면 누락이 된 데이터가 있을 수 있음으로 완벽한 파일을 못 다운로드를 할 가능성이 크다.    
>      
> 만약에 실시간 스트리밍(영상) 서비스가 있다고 과정하자.    
> TCP 방식으로 통신을 한다면 못받은 `패킷은 재 요청`을 해야한다. 그리고 `시간에 대한 지연`이 생긴다. 그 뜻은 영상이 끊기고 시간이 지난 후 다시 완벽한 영상을 보여 줄 것이다.    
> UDP 방식으로 통신을 한다면 못받은 패킷은 `무시`하고 받은 패킷만으로 통신을 하기 때문에 영상이 부드럽게 진행 될 것이다. 물론 누락이 있겠지만 빠른 속도로 통신을 하니 큰 영향이 없다.    