# 예외가 발생할 가능성이 있는 구문을 try로 감싼다
# 예외가 발생할 경우 처리할 구문을 except에 적는다
# except 다음에는 예외 종류를 적는다

# 에외 종류
# 1. Exception : 모든 에외들의 부모
# 2. IndexError : 인덱스가 범위를 벗어날 때
# 3. KeyError : 딕셔너리에 없는 키를 찾을 때
# 4. IntentaionError : 들여쓰기 에러
# 5. ZeroDivisionError : 0으로 나누었을 떄



# 예제 1
# num = 0
# try:
#     num = int(input())
# except ValueError: # value이 이상할 경우
#     num=0
# else:  #에러안났을때 구문
#     print(num)
# finally: # exception/else 상황에 관계없는 정리 문구. 에러로 인해 반환받은 num 값을 보여줌
#     print(num)



# 예제 2
# list=[1,2,3]
# value=0
# try:
#     index=int(input())
#     value=list[index] # 입력받은 값이 list의 index가 됨
# except (ValueError,IndexError): # 이상한 값을 입력하거나, list에 있는 index가 아닌경우
#     value=list[0] # list의 첫번쨰 값을 할당함 = 1
# print(value)



# 예제 3
# num=int(input())
# try:
#     value=10/num
# except ZeroDivisionError: # 만약 num이 0인 경우 = 0으로 나눴을 경우
#     print('devision by zero')
# else:
#     print(value)


# 예제 4
# num=int(input())
# try:
#     value=10/num
# except ZeroDivisionError as err:
#     print(err) # devision by zero 가 출력됨 ㅋㅋ
# else:
#     print(value)



# 실습 : 0,1    1,0  등을 입력하여 두 가지 에러를 각각 발생시켜보자
dict={1:'one', 2:'two'} # [] : array , () : tuple , {} : dictionary
num1 = int(input())
num2 = int(input())
try:
    value=10/num1
    value2=dict[num2]
# except (ZeroDivisionError, KeyError): #처음에 0을 입력하거나 , dict에 없는 key값을 입력할 경우
#     print('error')
except ZeroDivisionError as err1: # 이 에외가 먼저 처리되므로 뒤에 예외가 있어도 처리되지 않는다.
    print(err1)
except KeyError as err2:
    print(err2) # 입력한 key값이 나온다 
else:
    print(value, value2)
