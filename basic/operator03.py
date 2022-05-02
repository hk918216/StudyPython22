# 문자열 포맷팅
name = '도레미'
login_str = '{0}님 로그인중'.format(name)

print(login_str)

# 문자열 포맷팅 방법
print('{0}, {1}, {2}'.format('하나', 2, True))
print(f"{'하나'}, {2}, {True}")
print(f"{'하나'}, {2}, {login_str}") # {} 안에 변수값 넣을 수 잇음

#소수짐 표현
PI = 3.14159268
print('{0:0.2f}'.format(PI))
print(f'{PI:0.3f}')

full_name = 'Seong HG'
print(full_name.split()) # 문자열을 ' '으로 잘라서 리스트로 

greeting = 'Hello, World'
words = greeting.split(',') # 문자열을 ,로 잘라서 리스트로
print(words)

hi = '    Hello~    '
print(hi.lstrip())  #oracle LTRIM()  왼쪽 공백 삭제
print(hi.rstrip())  #oracle RTRIM()  오른쪽 공백 삭제
print(hi.strip())   #oracle TRIM()  양쪽 공백 삭제
print(words[1].strip()) #words[1] = World - 인덱스 [1] 위치가 World

#문자열 특정 단어. 문자열 값 변경
print(full_name.replace('Seong', 'Ashley'))

#리스트 연산
arr = [1,2,3,4,5]
print(arr[3] + arr[0])  # 그냥 숫자 4 + 1 

#arr = [1,2,3,'4',5]
#print(arr[3] + arr[0])   ## ERROR '4'가 문자열이기때문

arr = ['1',2,3,'4',5]
print(arr[3] + arr[0])  # 문자열 두개가 합쳐짐. 문자 4 1 출력. '4' 글자와 '1'글자 합쳐라

arr = [1,2,3,'4',5]
print(arr[3] * arr[2])  #'4'글자를 3번 반복 출력

# 이중 리스트
arr2 = [1, 2, 3.14, ['Hi', 'My', 'Friends']]
print(arr2[3][1]) 
print(arr2[3][1][0]) #My에서 M. My도 배열이기 때문에.

arr3 = arr + arr2
print(arr3)