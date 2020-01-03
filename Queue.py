#데이터를 저장하는 구조. 가장 먼저 넣은 데이터를 먼저 꺼낼 수 있다. (first in first out)
# like 터널
# 키보드 , 터치 이벤트 처리 등에 사용됨.

# Queue의 주요 연산
# put : 데이터 추가
# get : 데이터 꺼내기

# 주요 데이터
# front : 앞. 데이터를 꺼내는 쪽
# rear  : 뒤. 데이터를 넣는 쪽

queue = []
def put(value):
    queue.append(value) # 파이썬 리스트에 필요한 기능들이 다 구현되어 있음
def get():
    value = queue.pop(0) # queue[0]을 반환, index -1
    return value

while True:
    v = int(input())
    if v == 0:
        break # 0 입력시 종료
    else: put(v) # 아니면 put() 호출하여 입력값을 리스트에 추가

length = len(queue)
for i in range(length):
    print(get())
