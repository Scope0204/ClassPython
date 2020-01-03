# 고차 함수 : 함수를 다루는 함수
# 함수를 파라미터로 받을 수 있어야 하고 함수를 반환할 수 있음

def add(first, second):
    return first+second
def sub(first, second):
    return first-second

def executor(func, op, param1, param2):
    return func[op](param1, param2)

func = {'+': add, '-':sub}
print(executor(func, '+', 1,2)) #  3
print(executor(func, '-', 1,2)) # -1

def get_func(op):
    if op == '+':
        return add
    else:
        return sub

result = get_func('+')(1,2)
print(result)
