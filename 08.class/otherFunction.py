class Circle:
    def __init__(self , x=0 , y=0 , r=1):
        self.x=x
        self.y=y
        self.r=r
    # 객체가 없어질 때 호출
    def __del__(self):
        print('delete Circle')

    # print()로 객체 출력 시 원하는 내용을 지정.  java의 toString함수 역할
    def __repr__(self):
        return 'circle'

    # 산술연산자를 사용할 수 있게 해 줌 +
    def __add__(self, other):
        return self.x+other.x , self.y+other.y
    # 산술연산자를 사용할 수 있게 해 줌 -
    def __sub__(self, other):
        return self.x-other.x , self.y-other.y

    # 비교연산자를 사용할 수 있게 해 줌 ==
    def __eq__(self, other):
        if self.r == other.r and self.x == other.x and self.y == other.y:
            return True
        else:
            return False

c1 = Circle()
c2 = Circle(1,1,2)
print(c1 , c2)
print(c1+c2 , c1-c2)
print(c1==c2)
