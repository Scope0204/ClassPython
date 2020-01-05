# # 자식 클래스는 부모 클래스의 변수오 함수를 포함한다.
# # 부모 클래스
# class Member:
#     def __init__(self):
#         self.memberid='0'
#     def __repr__(self): #__repr__ : print()시 출력 시 원하는 내용 지정
#         return 'memberid='+self.memberid
#
# # 자식 클래스
# # 클래스 이름 뒤 괄호에 부모 클래스 이름을 적어 상속 받음
# class Student(Member):
#     pass
#
# s = Student() # 상속된 Member를 받음
# print(s)




# 자식클래스에 __init__이 있는 경우 부모의 __init__이 자동으로 호츨되지 않음. 따라서 명시적으로 불러줘야 한다
class Member:
    def __init__(self):
        self.memberid='0'
    def __repr__(self):
        return 'memberid='+self.memberid

class Student(Member):
    def __init__(self, major='computer'):
        super().__init__(); # 이 줄이 빠지면 memberid를 사용할 수 없다.
        self.major=major

s = Student()
print(s.memberid , s.major)
