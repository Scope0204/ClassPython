# var1 = int(input())
# var2 = int(input())
#
# if var1 >= 0 and var2 >=0:
#     print("OK")
# elif var1 < 0 and var2 <0:
#     print("NG")
# else:
#     print("SOSO")

# var = int(input())
# if var%2 == 0 :
#     if var ==0:
#         print("0")
#     else :
#         print("짝")
# else :
#     print("홀")


# var = input()
#
# if 4<=len(var)<=10 :
#     print("OK")
# else:
#     print("NG")

#삼항연산자
# var1 = int(input())
# var2 = int(input())
# print("OK") if var1+var2 >= 0 else print("NG")

#for문
# arr = [1,2,3,4]
# for i in arr:
#     print(i)
# for i in [2,4,6,8]:
#     print(i)
# for i in arr[2:]: #파이썬 slicing -> 특정 시작위치부터 끝까지 가져오기 arr[2] ~ arr[3] -> 3,4
#     print(i)      #반대로는 arr[:end] -> arr[0] ~ arr[end]

#튜플을 이용한 for. 튜플이란? 한번 생서외면 값을 변경할 수 없음. 튜플명=()
# tp = (1,2,3,4,5)
# for i in tp:
#     print(i)

#문자열을 이용한 for
# str = 'Hello everyone'
# for s in str:
#     print(s)

# arr = [1,2,3,4,5,6,7,8]
# for i in arr:
#     if i%2 == 0:
#         print(i)


# arr = [1,2,3,4,5,6,7,8,9]
# a = 0
# b = 0
# for i in arr:
#     if i%2 == 0 :
#         a += i
#     else :
#         b += i
# print(a , b)


# range() : 리스트 없이 일정 횟수만 반복하고 싶을 떄 사용
# for i in range(5): # 0 ~ 5-1
#     print(i)
# for i in range(5,10): # 5 ~ 10-1
#     print(i)
# for i in range(0,10,2): # (start,end,step) -> 0 2 4 6 8  이것도 end-1까지
#    print(i)

#구구단 2단
# for i in range(1,10):
#     print(2*i)

# 지금 출력 중인 아이템의 index가 꼭 필요할 떄 : enumerate
# for index, value in enumerate([0,2,4,6,8,10]): #첫번쨰 변수(index)가 index가 된다
#     print(index,value)

# 두 개 이상의 리스트 사용하기 : zip , 같은 길이의 리스트에 대해서 index에 해당 하는 값을 모든 리스트에서 가져옴
# arr1 = [1,2,3,4,5]
# arr2 = [9,8,7,6,5]
# arr3 = [10, 20, 30, 40, 50]
# for i,j in zip(arr1,arr2):
#     print(i,j)
# for i,j,k in zip(arr1,arr2,arr3):
#     print(i,j,k)

# 딕셔너리 내부에서 for문을 사용하여 초기화 하기 : Dictionary comprehension
# arr_id = ['학생1' , '학생2' , '학생3' , '학생4', '학생5']
# arr_score = [80, 70, 90, 70, 80]
# dic = { key : value for key , value in zip(arr_id , arr_score)}
# dic2 = { key : value for key , value in zip(arr_id , arr_score) if value > 80}
# print(dic)
# print(dic2)
