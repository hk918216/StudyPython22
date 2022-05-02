# if문 
name = '홍길동'
gender = '남'

if name == '홍길동':
    if gender == '남':
        print('진료실로 들어갑니다.')
        print('의사쌤한테 인사합니다')  # 들여쓰기 주의하기. 줄맞추기 중요
    else:
        print('성별이 다르네요~')
else:
    print('부를때까지 기다리세요')
    print('궁시렁거립니다')

# 문장 줄이기 and 사용
if name == '홍길동' and gender == '남':
    print('진료실로 들어갑니다.')
    print('의사쌤한테 인사합니다') 
    
else:
    print('부를때까지 기다리세요')
    print('궁시렁거립니다')


num = 10

if num !=9:
    print('9가 아닙니다')
else:
    print('9입니다')


