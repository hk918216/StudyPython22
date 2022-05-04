# 파일 입출력 2 - 파일 읽기

f =open(file='./temp.txt', mode='r', encoding='utf-8') #상대경로사용

# t = f.read()
while True:             #무한루프
    line = f.readline() #
    if not line: break  #읽을게 더이상 없으면 탈출

    print(line, end='')

f.close  #필수!
print('파일 읽기 완료')

