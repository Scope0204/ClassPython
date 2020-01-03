# def abs(value):
#     return [v if v >0 else -v for v in value]
#
# print(abs([1,2,3,-1,-2,-3]))
# print(abs(i for i in range(-3,3)))
# print((i for i in range(-3,3)))




# yield : generator를 만드는 함수
# def my_gen(n):
#     for i in range(n):
#         yield i * 10

# list = [i for i in my_gen(5)]
# print(list)
# gen = my_gen(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen)) # 길이 이상으로 호출하면 예외 발생




def my_range(*num):
    step=1
    params = len(num)
    if params == 1:
        start=0
        end=num[0]
    elif params > 1:
        start=num[0]
        end=num[1]
        if params > 2:
            step = num[2]
    while start < end:
        yield start
        start += step

list1 = [i for i in my_range(5)]
list2 = [i for i in my_range(2,5)]
list3 = [i for i in my_range(1,10,2)]

print(list1)
print(list2)
print(list3)
