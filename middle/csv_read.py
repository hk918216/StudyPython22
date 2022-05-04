# CSV파일 읽기
import csv

file_name = 'busanbus_211231.csv'  

f = open('./'+file_name, mode= 'r', encoding='utf-8')
reader = csv.reader(f, delimiter=',')  #구분자가 , 일 경우
next(reader)  #제목줄(헤더) 있는경우 헤더가 필요없을때 사용

for line in reader:
    print(line)

f.close()