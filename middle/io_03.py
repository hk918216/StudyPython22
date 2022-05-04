# 입력값 다중으로 받기. 두개의 값 입력받아 두개의 변수에 나눠담기
x, y, z = input('세 단어를 입력하세요(구분자는 /) > ').split('/')
print(x)
print(y)
print(z)


x, y = input('두 수를 입력하세요(구분자는 /) > ').split('/')
print(int(x) * int(y))                   #print에서 형변환


x, y = map(float, input('두 수를 입력하세요(구분자는 /) > ').split('/'))   #형 변환
print(x * y)


greeting = "Hello, I'm a student. \"Bye~\" "  # " "안에 " " 사용하려면 \" 사용
print(greeting)