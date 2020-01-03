# def hello():
#     print("hello")
# hello()


# 값 전달, 두개 이상은 콤마로 구분
# def hello(name):
#     print("hello" , name)
# hello('준경스?')


# 정수 2개를 입력받아 더 큰 값이 나오는 것을 출력
# def bigger(a,b):
#     if(a>b):
#         print('a가 더 크다 값은 : ' , a)
#     elif(b>a):
#         print('b가 더 크다 값은 : ' , b)
#     else:
#         print('같음')
# a = int(input())
# b = int(input())
# bigger(a,b)


# 값을 주지 않는 다면 기본값을 사용할 수 있음
# def hello(age, name='user'): # 기본값을 사용하는 파라미터는 가장 뒤에 넣는다
#     print('hello', name , age)
#
# hello(20) # 기본값인 user가 나온다.
# hello(20 , 'abc')



# 갯수를 정하기 어려울때는 * 또는 ** 를 넣는다
# * -> 튜플로 전달 / ** -> 딕셔너리로 전달
# def print_tp(*t):
#     print(t)
#
# def print_dn(**d):
#     print(d)
#
# print_tp(1,2,3,4,5)
# 딕셔너리로 주고 싶으면 key에 해당하는 변수 이름도 줘야함
# print_dn(first=1, second=2, third=3)



# 가변 길이의 변수를 받아 그 중 정수만을 골라 합을 출력하는 함수
# def sum_int(*number):
#     sum = 0
#     for v in number:
#         if type(v) is int: # type() : 특정 값의 데이터 타입을 알 수 있는 함수 , is 키워드로 체크
#             sum += v
#     print(sum)
# sum_int(1,1,1.0,'1',True)


# 가변 변수와 일반 변수 함께 사용하기
# def param1(a, *t, b , c =3):
#     print(c) # 3
#     print(t) # (2,3)
# param1(1,2,3,b=4)



# * , ** 를 이용하여 리스트나 튜플, 딕셔너리를 개별 파라미터로 나누어 사용할 수 있다.
# def func(first , second):
#     print(first, second)
# param1=[1,2] #리스트
# param2=(3,4) #튜플
# func(*param1)
# func(*param2)
# func(*[5,6]) # 리스트라 * 써야하는 듯?
# dict = {"first":1 , "second":2} # 딕셔너리
# func(**dict)



# 정수 리스트에서 최소값을 반환하는 함수
# def min_int(list):
#     min = list[0]
#     for i in list[1:]: #slicing -> 특정 시작위치부터 끝까지 가져오기 list[input] ~ list[end]
#         if i < min:
#             min = i
#     return min
#
# list = [1,2,3,4,5,6,7,8,9,10]
# print(min_int(list))




# 튜플 타입을 반환 받을 시 튜플로 받을 수도 있고 , 각각의 변수로 나누어 받을 수도 있다.
# def tuple():
#     return 1,2,3; # 튜플은 ()를 안하고 , 로 구분해도 튜플로 인정받는다
#
# tp = tuple()
#
# print(tp , type(tp))
# x,y,z = tuple()
# print(x,y,z, type(x))
# 튜플 값 중 하나를 일반 변수에 저장한 것이라 값을 변경할 수 있음
# x = 10
# return되는 튜플 값중 일부만 필요할 때는 다음과 같이 사용
# x , _ , z = tuple() # 반환 받으려면 무조건 갯수만큼 채워 넣어야함



#정수 리스트를 파라미터로 받아 합계와 평균을 반환하는 함수
# def info(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum , sum/len(list)
#
# list = [1,2,3,4,5,6,7,8,9,10]
# sum , avg = info(list)
# print('sum=',sum , 'avg=' , avg)




정수 리스트를 파라미터로 받아 최대 최솟값을 반환하는 함수
def min_max(list):
    max = list[0]
    min = list[0]
    # for i in list: #혹은
    for i in list[1:]:
        if max < i:
            max = i
        if min > i:
            min = i
    return max,min

list = [1,2,3,4,5,6,7,8,9,10]
max , min = min_max(list)
print('max = ' , max , 'min = ' , min)
