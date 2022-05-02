# for문 학습

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0 

for x in arr:
    result = result + x

print('배열의 합 =', result)

# 1~100까지 더하기
for x in range(1,101):    # (시작하는 숫자, 마지막 숫자+1).
    result = result + x

print('배열의 합 =', result)

arr2 = ('me', 'my', 'friend', 'Jane') #()든 []이든 상관없음

for i in arr2 :
    print(f'{i:>10}')   #글자자리를 10자리로 만들어서 들여쓰기. 10자리 미만이면 왼쪽에 공백생김

for i in arr2 :
    print(f'{i}')

##1~10까지 수에서 짝수 구분하기
for num in range(1,11) :
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다')    #print(num) 가능
    else :
        print(f'{num}는 홀수입니다')

for num in range(1,11, 2) :  # 1부터 10까지 2씩 증가
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다')    
    else :
        print(f'{num}는 홀수입니다')


# for문 내에서 사용하는 continue, break
values = [1,3,5,7,9,11,13,15,17,19]
num = 0

for item in values :
    num += 1 # num = num +1
    if (num % 2) == 0 :
        #break  #반복문 탈출
        continue #if 조건만 패스 후 다음 값 진행
    else:
        print(f'{num}번 수는 {item}입니다')


