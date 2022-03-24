# new
> new는 한가지의 모델의 오브젝트를 생성한다. User.new, User.new(name: 'peko', type: 'human') 형식으로 선언 가능하다.     
    
# all
> all은 그 모델의 모든 객체(레코드)를 반환한다. User.all과 같은 형식으로 선언 가능하다.      
     
# find
> 만약 User이라는 모델이 있으면 User.find(1)을 하면 user.id = 1 인 레코드를 찾아준다. 없을시 `에러`가 난다.     
> 단 한개의 `오브젝트`만 반환한다
       
# find_by
> 만약 User이라는 모델이 있으면 User.find_by(id: 1)을 하면 user.id = 1인 레코드를 찾아준다. User.find_by(name: 'peko')인 경우도 가능하다. 없을시 `nil`을 반환 한다.     
> 단 한개의 `오브젝트`만 반환한다. 한가지의 오브젝트를 `에러`없이 검색하고 싶을때 사용하자.     
    
# where
> SQL의 where과 같다. User.where(id: [1,2,3,4,5]) User.where(type: people)과 같은 형식으로 검색한다.      
> ActiveRecord array형식으로 오브젝트가 반환된다. 없을경우 nil을 반환한다.     
    
# create
> create는 DB에 객체를 저장한다.    
> 사용법은 User.create(name: 'peko', type: 'people')과 같다. 성공시 객체를 반환한다.    
    
# update
> update는 한 객체의 속성을 수정하고 그 객체의 레코드를 갱신한다.   
> user = User.find_by(name: 'pako')   
> user.update(name: 'peko')과 같다.   
> 한가지의 객체만 update를 할 수 있다.    
    
# destroy
> destroy는 그 객체의 레코드를 삭제한다.   
> user = User.find_by(name: 'pako')    
> user.destroy과 같다.    
> 한가지의 객체만 destroy를 할 수 있다.    
    
# destroy_by
> destroy_by는 모델의 테이블에서 `검색`하고 그 결과의 레코드를 전부 삭제한다.    
> User.destroy_by(type: 'humman')과 같다.     
    
# destroy_all
> destroy_all은 모델의 테이블에 있는 레코드를 `전부 삭제한다.`    
> User.detroy_all과 같다.    
    
# save
> save는 단일 객체의 레코드를 `생성 또는 갱신한다.` 생성 갱신 성공 또는 실패 시 True False를 반환한다.   
> user = User.new(name: 'pako', type: 'humman')     
> user.save 이와 같은 경우는 생성이되며 성공시 True 실패시 False     
> user.name = 'peko'   
> user.save 이와 같은 경우는 갱신이되며 성공시 True 실패시 False    
> save!를 사용하면 강한 검사(validate등)을 한다. 만약 실패한다면 에러가 발생된다.     

# order
> SQL order by 와 같다. 정렬을 해주는 것 이라고 생각하자.
> User.all.order(:name)
> User.all.order('name desc') 와 같이 사용하다.
> 만약 User와 Phone이 1:1관계일때 User을 Phone번호로 order할 경우에는
> User.all.order(phone.phone_number)과 같이 정렬도 가능하다.
