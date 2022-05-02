# 문자열
from operator import truediv


bruce_eckel = 'Life is short, You need a Python.'
print(bruce_eckel)

bruce_eckel = 'Life is short, \nYou need a Python.'   # \n 문자열바꾸기  \t 탭(들여쓰기)
print(bruce_eckel)

#여러줄 문자열 - 문자의 배열. 역시 리스트이다

multi_line = '''Life is short,
You need Python.
And I need C#, too. 
'''                                         #'''(홑따움표 세번) 사용해도 줄 바뀜
print(multi_line)

# 리스트(배열) []
b = [1,2,3,4]
print(b)

b.append(5)   #리스트 맨 마지막에 괄호 속 값 추가
print(b)  

b.insert(3, 10)   # 원하는 위치에 인덱스 추가
#3번째 위치에 10을 넣겠다. 시작 위치 나타내는 숫자 0으로 시작. 즉, 여기서 3은 4번째 위치를 말함
print(b)

b.sort()  #오름차순 정렬
print(b)

b.reverse()  #내림차순 정렬
print(b)

b.remove(10)  # 원소 삭제
print(b)

print(type(b))

#튜플 ()
c = (1,2,3,4)
print(c)

#c.append(5) erroe 튜플에서 값 추가 불가
print(c[2]) #2번째위치에 있는 값 출력


#딕셔너리 key : value 쌍의 집합. {}
spiderman = {
    'name' : '피터 파커' ,
    'age' : 18 ,
    'weapon' : '웹슈터' ,
    'memberOFAvengers' : True
} 
print(spiderman)
print(spiderman['name'])
print(spiderman['memberOFAvengers'])


