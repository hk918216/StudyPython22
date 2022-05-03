#구구단 프로그램
# 2x1 =2 ... 2x9 =18   x * y = xy
# 3x1 =3 ... 3x9 =27
# .......... 9x9 =81

print('---구구단 프로그램--- \n')
'''for x in range(2,10) :
    for y in range(1,10) :
        print(f'{x}*{y} = {x*y:2d}', end=' ')  #한줄로 출력됨 # ':2d' = 두자리수 숫자 감안해서 자리만들기'''


for x in range(2,10) :
    print(f'{x}단 시작')
    for y in range(1,10) :
        print(f'{x}*{y} = {x*y:2d}', end=' ')
    print()   # 단 마다 줄 맞춰주기. 한줄로 나오는 출력을 보기쉽게 나누기 위해. 
              # print('\n') - 사용하면 단이 끝나고 공백생긴 뒤 'n단시작' 출력