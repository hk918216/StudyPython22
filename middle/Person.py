# 사람객체를 위한 클래스 Person
from unicodedata import name


class Person:
    __name = ''   #이름속성
    age = 0       #나이속성
    heigh = 100   #키
    weight = 30   #몸무게

    #생성자 재정의
    def __init__(self, name = None) -> None:
        if name == None:
            self.__name = '홍길동'
        else :
            self.__name = name
        print(f'{self.__name} 탄생!!')

    #매직메소드 __str__ 사용 재정의
    def __str__(self) -> str:
        value = f'''객체 {self.__name}
나이 : {self.age}
키 : {self.heigh}'''
        return value

    def walk(self, speed) :
        print(f'{self.__name}이(가) {speed}km/h로 걷는다.')
        return

    def run(self, speed):
        print(f'{self.__name}이(가) {speed}km/h로 뛴다.')


p = Person('성혜경')  # 객체생성 #Person() 이 비어있으면 홍길동 나옴
# p.__name = '성혜경'
p.age = 25
p.heigh = 180
p.weight = 75

p.walk(2)
p.run(10)
#print(type(p))
print(p)