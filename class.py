# class 키워드를 사용해 클래스 선언
# 파이썬의 다른 변수들과 달리 클래스 이름의 첫 글자는 대문자를 주로 사용
# __init__ 함수에서 초기화를 진행할 수 있음
# __init__ 함수의 파라미터로 전달되는 self가 자바의 this 역할을 함

class MyClass:
# 파이썬은 첫 번째 파라미터로 self를 받음
    def __init__(self, message):
        print(message)

# new 키워드 없이 클래스 이름의 함수를 호출하면 객체가 생성되어 할당 됨
value = MyClass('hello')
