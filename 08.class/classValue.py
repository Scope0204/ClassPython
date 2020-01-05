# 클래스 변수에는 크게 2가지가 있음
# 1. 클래스에 선언하는 변수 : 클래스의 모든 객체들이 공유하는 변수
# 2. self에 선언하는 변수 : 하나의 객체만 전용으로 사용하는 객체 변수


# class MyClass:
#     message='hello'
#     def __init__(self ,name):
#         self.name=name
#
# print(id(MyClass.message))
# # id() : 객체를 입력값으로 받아 객체의 고유값(레퍼런스)을 반환하는 함수
# a=MyClass('a')
# print(a.name, id(a.name) , a.message , id(a.message))
# b=MyClass('b')
# print(b.name, id(b.name) , b.message , id(b.message))
# MyClass.message='bye'
# print(a.message, b.message)




#클래스 변수를 클래스 이름이 아닌 객체에서 변경할 경우 immutable변수는 복제본이 생기고 원본이 변경되지 않고 muttable인 경우 원본이 변경된다.
# mutable은 값이 변한다는 뜻이고, immutable은 값이 변하지 않는다는 의미이다.
class MyClass:
    str ='hello'

a=MyClass()
b=MyClass()

MyClass.str='bye'
print(a.str , b.str)
#클래스 변수를 클래스 이름이 아닌 객체에서 변경할 경우
a.str='a'
print(id(MyClass.str) , id(a.str) , id(b.str))

class MyArrClass:
    arr=[1,2,3] #리스트 , muttable
c=MyArrClass()
d=MyArrClass()
MyArrClass.arr.append(4)
print(c.arr,d.arr)
c.arr.append(5) #그러나 d도 할당됨,  muttable인 경우 원본이 변경된다.
print(c.arr,d.arr)
print(id(MyArrClass.arr) ,id(c.arr))
