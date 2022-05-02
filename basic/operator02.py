# 문자열 연산
first = 'Hello'
second = 'World!'

print(first + second)    #문자연산 +(합치기)
print(first, second)  # 콤마 사용하면 띄어써짐. concat

print(first * 3) # 횟수만큼 문자열 반복

# 문자열 길이 내장함수
print(len('한글'))
print(len(first))

#리스트 연산
print(first[-1])  #마지막 문자부터 -1
print(first[-2])  
print(first[-3])  
print(first[-4])  
print(first[-5])  
# print(first[-6])  - indexerror! 큰문제 

# 현재일시
current_date = '2022-05-02 14:23:45'
year = current_date[0:4]  #0부터 시작하는건 0 생략 가능
month = current_date[5:7]  #[인덱스 위치 : 실제 위치]
day = current_date[8:10]
hour = current_date[11:13]
min = current_date[14:16]
sec = current_date[17:19]

print('년 : ', year)

print(year, '년', month, '월', day, '일')
print(hour, '시', min, '분', sec, '초')

print(current_date[-5:-3])  #-5,-4번째 값 출력

l = [1,2,3,4,5]
l[0] = 10
print(l)

p = 'python'
print(p)
# p[0] = 'P' # TypeError
print('P' + p[1:])  # 대문자 P 뒤에 ython 더하기

p2 = 'P' + p[1:]
print(p2)

print(p.upper()) #대문자로 바꾸기
print(p2.lower())