stack=[None for i in range(10)]
size=len(stack)
top= -1

def push(value): # top을 1증가시키고 size를 넘지 않으면 데이터를 추가
    global top
    if top < size-1:
        top += 1
        stack[top] = value # 새 데이터의 index가 top이 된다. stack[top] = 새 데이터 value
        return top
    else:
        return None # 데이터를 넣을 공간이 남아있지 않는 경우 None을 반환한다

def pop(): # 현재 top이 가리키는 데이터를 꺼낸다음 top이 그 아래 데이터를 가리키도록 함. 꺼낸 데이터를 반환
    global top
    if top > -1: # 데이터의 index는 0 부터이므로 -1 보다 큰 것 밖에 없다
        value = stack[top]
        del stack[top] # del stack[top]은 top번째 요솟값을 삭제한다. -> top이 가리키는 데이터를 꺼낸다
        top -= 1 # 데이터를 꺼냈으므로 top index를 하나 줄인다
        return value
    else:
        return None # 꺼낼 데이터가 없으면 None을 반환한다

while True:
    print('---------------')
    print('1:push\n2:pop\n0:finish')
    s = input()
    if s == '1':
        print('number:' , end=' ')
        num = int(input())
        print('pushed' if push(num) != None else 'stack overflow') # 10번쨰 이후 데이터 기입부터 None을 반환해 else문 메시지가 뜬다
    elif s == '2':
        num = pop()
        print('php:' + str(num) if num != None else 'stack empty') # 꺼낼 데이터가 없는 경우 None을 반환해 else문 메시지가 뜬다
    elif s == '0':
        break

#파이썬의 list는 이러한 스택의 기능을 구현하고 있다.
# push -> list.append(value)
# pop  -> list.pop() 
