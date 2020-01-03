# 이진 탐색
# 정렬 된 리스트가 주어질 때 그 리스트 안에 내가 찾는 값이 있는지 확인 하는 것이 탐색
# 그 중 주어진 리스트를 반으로 나누어가며 찾는 것이 이진 탐색


def b_search(value, list, low, high):
    if low > high:
        return -1
    mid = (low+high)//2  # // : 좌항을 우항으로 나눔(정수형)  Ex] 10 // 3 = 3
    if list[mid] == value:
        return mid
    if list[mid] > value:
        return b_search(value, list, low, mid-1)
    else:
        return b_search(value, list, mid+1, high)

list=[1,3,6,9,12,15,18,21]
print('result index=', b_search(15, list, 0, 7))

def b_search(value, list): # 오버로딩
    low, high = 0 , len(list)
    while low <= high:
        mid = (low+high)//2
        if list[mid] == value:
            return mid
        if list[mid] > value:
            high = mid -1
        else:
            low = mid + 1
    return -1

list = [1,3,6,9,12,15,18,21]
print('result index=' , b_search(15,list))
