# 병합 정렬
# 리스트의 길이가 1이면 정렬이 된 상태임
# 정렬이 된 두 리스트를 병합(merge)하면 그 결과는 역시 정렬 된 상태가 된다
# 모든 리스트를 정렬할 떄 까지 2를 반복한다.


# 병합 방법
# 병합 할 두 리스트는 정렬 된 상태이기 때문에 각각의 리스트 제일 앞의 수가 가장 적은
# 이를 반복하여 두 리스트를 하나의 결과 리스트로 만들면 병합 완료.


def merge(list, low, mid, high):
    l = low
    r = mid+1
    temp = []
    while l <= mid and r <= high:
        if list[l] < list[r]:
            temp.append(list[l]) # append()는 object를 맨 뒤에 추가
            l += 1
        else:
            temp.append(list[r])
            r += 1
    if l > mid:
        temp.extend(list[r:high+1]) # extend()는 객체(리스트,튜플,딕셔너리 등)의 엘리멘트를 list에 append 시킴
    elif r > high:
        temp.extend(list[l:mid+1])
    list[low:high+1] = temp
    print(list)

def merge_sort(list, low, high):
    if low >= high:
        return
    mid = (low+high)//2
    merge_sort(list, low, mid)
    merge_sort(list, mid+1, high)
    merge(list, low, mid, high)

list = [8,7,6,5,4,3,2,1]
merge_sort(list, 0 ,7)
