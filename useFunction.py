# 파이썬에서 함수 이름은 함수의 포인터와 같이 동작
# def func():
#     print('hello')
# func() # hello
#
# def func(): #기존 정의를 대체함
#     print('bye')
# func() # bye

selection = int(input())
if selection == 1: #입력한 값이 1인 경우
    def func(): # 함수 이름을 변수처럼 사용할 수 있다.
        print('hello')
else: # 입력값이 1외의 다른 수일 경우
    def func():
        print('bye')

func()
