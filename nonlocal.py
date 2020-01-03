# 중첩 된 함수에서 자신의 부모 함수에 선언된 변수를 사용할 때는 nonlocal 키워드를 사용
# 단, 외부 함수의 값을 수정하지 않고 읽기만 할 경우에는 nonlocal키워드 없이 사용 가능함
def func():
    value=2
    def nested_func():
        nonlocal value # func의 value를 참조
        value=3
        print('nested' , value)
    nested_func()
    print('outer' , value)

func()
