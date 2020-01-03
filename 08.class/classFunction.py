# 클래스에 소속된 함수는 다음과 같이 클래스 선언에 들여쓰기를 하여 선언 가능
# 첫 번째 파라미터로 self를 받아야함
# 호출은 클래스 객체에서 .을 찍은 다음 호출할 수있다

class MyClass:
    def __init__(self):
        pass
        # pass : 단순히 실행할 코드가 없다는 것을 의미
        # continue : 다음 순번의 loop를 돌도록 강제하는 것을 의미

# 첫 번째 파라미터로 self를 받아야함
    def say_hello(self):
        print(message)

my=MyClass()
my.say_hello()
MyClass.say_hello(my) # 객체가 아닌 클래스 이름으로 함수를 불러 쓸 수도 있음
                      # 단, 이경우 self에 해당하는 객체를 명시적으로 파라미터로 넘겨줘야함
