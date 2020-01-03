# while True:
#     print('Enter number:' , end='')
#     value = int(input())
#     if value < 0:
#         break


# for i in range(4):
#     print('i=' , i , end=', ')
#     for j in range(4):
#         print('j=' , j , end=' ')
#         if j > 0: # 0 다음 1까지는 출력 되겟지유?
#             break
#     print('')


# val = 1
# while val > 0:
#     val = int(input())
#     if val > 10:
#         break;
#     else:
#         print('more')


#continue : 반복문 처음으로 이동 , pass : 해당 문구 차례에 아무 일도 하지 않음
# sum = 0
# for i in range(5):
#     val = int(input())
#     if val < 1:
#         pass # 1이하는 if , else 조건문 실행을 안한다.
#     else:
#         sum += val
#     print('sum=' , sum)
# print('final sum=' , sum)


# 0 입력 전까지의 모든 수의 평균을 출력하는 법
# value_sum=0
# value = int(input())
# count=0
# while value != 0:
#     value_sum += value
#     count += 1
#     value = int(input())
# print(value_sum/count)
# # 리스트를 써서 하는 버전
# varr=[]
# value=int(input())
# while value != 0:
#     varr.append(value)
#     value = int(input())
# print(sum(varr)/len(varr)) #리스트 합 / 길이
