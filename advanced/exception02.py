# 예외처리 2 - 예외발생 2
x, y = map(int, input('두 수를 입력하세요 > ').split(' '))

print(f'x = {x}')
print(f'y = {y}')

try:
    z = x / y    # 이 z는 지역변수 안에서만 사용가능. try 구문 사용 후 z 사라짐. 지역변수이기때문
    print(f'{x} / {y} = {z}')
# except TypeError as e:
#     print('형 변환 하세요')
# except ZeroDivisionError as e:
#     print('두번째수에 0은 금물')
except Exception as e:
    print(f'예외발생 {e}')   # 모든 예외 다 적기보다 쉽게 알 수 잇음


print('나누기 종료')