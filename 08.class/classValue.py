# 클래스 변수에는 크게 2가지가 있음
# 1. 클래스에 선언하는 변수 : 클래스의 모든 객체들이 공유하는 변수
# 2. self에 선언하는 변수 : 하나의 객체만 전용으로 사용하는 객체 변수

class MyClass:
    message='hello'
    def __init__(self ,name):
        self.name=name

print(id(MyClass.message))
a=MyClass('a')
print(a.name, id(a.name) , a.message , id(a.message))
b=MyClass('b')
print(b.name, id(b.name) , b.message , id(b.message))
MyClass.message='bye'
print(a.message, b.message)
