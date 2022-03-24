# belongs_to
> belongs_to는 외래키를 가지고 있는 테이블이 선언한다.    
> `만약 User과 Phone 테이블과 모델이 존재한다.`   
> User은 name과 type 속성(컬럼)을 가지고 있다   
> Phone은 phone_number과 user_id를 가지고 있다. 이때 user_id는 user의 외래키 이다.    
> 이와 같이 1:n 1:1 관계 중에 외래키를 들고 있는 Model에게는 belongs_to를 사용한다.   
> belongs_to :user 과 같은 형식으로 선언한다. 이와 같이 선언 했을 경우 관계 참조가 편해진다.    
> phone = Phone.first, user = phone.user과 같이 사용 가능하다.    

# has_one
> 1:1의 관계일 경우 사용된다. has_one을 선언한 모델은 외래키를 가지고 있지 않아야 한다.   
> 한 사람당 핸드폰을 한개만 가질 수 있다. 그때 Phone과 User이 1:1관계이다.    
> 윗 belongs_to의 이야기를 참조하여 이야기를 해보면 Phone이 user_id를 가지고 있으며 User은 phone_id를 가지고 있지 않기 때문에 User모델에서는 has_one을 사용한다.    
> has_one :phone 과 같은 형식으로 선언한다.     
> phone = Phone.first, user = phone.user과 같이 사용 가능하다.    

# has_many
> 1:n 관계에 사용된다. has_many을 선언한 모델은 외래키를 가지고 있지 않아야 한다.   
> 예시로 User과 Item이 1:n관계이다    
> User 한명은 많은 Item을 가질 수 있다.   
> 이럴때가 1:n관계가 되는 것이다.     
> User은 하나이고 User가 가지고 있는 Item은 다수이니    
> User모델에서는 has_many :item`s`가 된다 `Rails에서는 영어 문법을 중요히 생각해 복수개 has_many와 같이 복수개 일 경우에는 s를 붙혀 줘야한다.`    
> Item모델에서는 belongs_to :user 이 된다.    

# through
> through는 두관계 이상의 관계 데이터를 한번에 참조 할 수 있게 해주는 기능이다.   
> 예시로 User과 Blog와 BlogFriend가 있다고 하자.    
> Blog는 user_id를 들고 있으며 User과 1:1 관계이다.   
> BloFriend는 blog_id를 들고있으며 Blog와 1:n 관계이다.   
> 이때 User이 BlogFriend를 참조하려면 아래와 같다.    
> user = User.find(1)   
> blog_friends = user.blog.blog_friend`s`(복수임으로)인 형식으로 불러올 수 있다.    
> 만약 User모델에 has_many :blog_friends, through: :blog(blog를 통해서 참조 하겠다라고 이해하면 편하다.)를 선언하면    
> user = User.find(1)   
> user.blog_friends처럼 선언 가능하다.    


