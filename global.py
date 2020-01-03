#함수 내에서 전역 변수를 사용하고 싶은 경우 glabal 키워드를 사용한다.
# sum = 0
# def total(values):
#     global sum #전역을 선언 되지 않은 변수에 global을 붙여 선언하면 전역 변수가 추가 된다
#     # 바로 선언해도됨
#     for i in values:
#         sum += i
#     print(sum)
#
# total([1,2,3])
# print(sum)




# 다만, 함수에서 전역 변수를 직접 수정하는 것은 구조적으로 위험 하므로 함수 리턴 값을 받아 최상위 레벨에서 전역 변수를 수정하는 것이 좋음
sum = 0
def total(values):
    sum = 0
    for i in values:
        sum += i
    return sum

sum = total([1,2,3])
print(sum)
