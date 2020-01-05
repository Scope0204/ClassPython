# overriding : 부모 클래스에 선언된 함수를 재정의 하는 것
# 함수 이름과 파라미터가 부모와 같아야한다.
# 오버라이딩 되면 기본적으로 자식의 함수 코드가 실행된다.
# 부모의 함수를 부를 때는 super()를 사용한다.

class Member:
    def __init__(self):
        self.memberid='0'
    def __repr__(self):
        return 'memberid='+self.memberid

class Student(Member):
    def __init__(self, major='computer'):
        super(). __init__();
        self.major=major
    def __repr__(self): # 함수 이름, 파라미터 모두 같다
        # return 'major='+self.major
        return super().__repr__() + ', major='+self.major

s = Student()
print(s) # Student class의 __repr__이 호출 됨
