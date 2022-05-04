#파일 입출력 1 - 쓰기

f = open('C:/STUDY/StudyPython22/temp.txt', mode='w', encoding='utf-8')  #절대경로사용
# mode = w 는 항상 새로 생성쓰기, a는 추가쓰기, r은 읽기

f.write('안녕하세요.\n')
f.write('저는 성혜경입니다.\n')
f.write('한국사람이죠.\n')

f.close()    # 필수!
print('파일 생성완료')