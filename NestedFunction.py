# 고차 함수는 함수안에 함수를 선언할 수 있다.
# 내부 함수는 외부에서는 바로 호출 할 수 없다.

def calculate(op, num1 , num2):
    def add(num1, num2):
        return num1 + num2
    def sub(num1 , num2):
        return num1 - num2

    if op == '+':
        return add(num1 , num2) # 이런 식으로 내부에서 호출
    else:
        return sub(num1 , num2)

print(calculate('+', 1,2))
# 즉 calculate 외부에서는 add()나 sub() 와 같이 사용할 수 없다.

# 외부에서 호출하는 경우
# print(add(1,2)) # add()가 정의되지않았다고 오류가 발생



# 기본적으로 각 함수는 자신이 선언한 지역 변수만을 사용할 수 있다
def func():
    value=2
    def nested_func():
        value=3
        print('nested',value)
    nested_func() # 먼저 실행
    print('outer' , value)

func()
