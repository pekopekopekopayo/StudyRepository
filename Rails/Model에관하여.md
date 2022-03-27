# Model에관하여

## after_create

> create를 끝내고 실행시킬 코드를 정의해야 할 때 사용

## before_save  before_create before_update before_destroy

> save create update destroy를 하기전에 실행시킬 코드를 정의해야 할 때 사용

## attr_reader

> 모델에 정의를 하며 그 모델에 가상적 컬럼을 만든다.  
> 처음에 컬럼 값은 설정이 가능하나 추 후에는 읽기(참조)만 가능하며 값을 변경 시킬 수 없다.

## attr_accessor

> 모델에 정의를 하며 그 모델에 가상적 컬럼을 만든다.  
> 가상적 컬럼의 값은 참조/갱신 가능하다.

## validates

> validates는 컬럼을 지정하고 그 컬럼의 유효값을 설정한다. 유효 값 설정은 Rails가 기본적으로 가지고 있는 옵션으로 설정 가능

## validate

> validate는 유효 값 설정을 method로 설정 할 때 사용한다.

## scope

> 잘 사용되는 Orm명령어(쿼리)을 이름으로 정의 할 수 있다.
