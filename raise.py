# 파이썬에서 지정한 예외가 아닌 개발자가 필요한 경우 예외를 일으키는 방법
def add(first, second):
    if not type(first) is int or not type(second) is int: # fitst 또는 second가 int 형이 아니면
        raise TypeError # 개발자 커스텀 에러
    return first+second


try:
    add('1',1) # first가 int형이 아님. str
except TypeError:
    print('not supported data type')
