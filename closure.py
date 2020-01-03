# 클로저란? 내부 함수를 반환할 때 외부 함수의 상태를 저장해 두었다가 나중에 사용
def scale_up():
    scale=10
    def calculate(number):
        return number*scale # 외부 함수의 값을 수정하지 않고 읽기만 할 경우에는 nonlocal키워드 없이 사용 가능함
    return calculate # 함수만 리턴함. 그러나 함수에서 외부 함수의 scale값을 참조하고 있음

func = scale_up()
print(func(10)) # 함수를 호출했을 때 외부 함수의 scale 값을 사용한 계산 결과가 나옴 , 100
