# 주소록 프로그램 ver.1.1
# 작성일 : 2022-05-04
# 작성자 : SEONG HG
# 설  명 : 주소록

import os

# 연락처 클래스
class Contact:
    name = ''; phone_num = ''; e_mail = ''; addr = ''  # =self.name / self.addr ... 이랑 같음

    def __init__(self, name, phone_num, e_mail, addr) -> None:   #윗줄 네임,폰넘버 .. 과 다름
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str:
        str_val = (f'이  름 : {self.name}\n'
                   f'핸드폼 : {self.phone_num}\n'
                   f'이메일 : {self.e_mail}\n'
                   f'주  소 : {self.addr}\n'
                   f'==============================')
        return str_val

def run():
    lst_contact = []     # 빈리스트 생성
    load_contact(lst_contact)  #파일DB 읽어오기
    clearConsole()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            contact = set_contact()
            if contact is None:
                input('계속하려면 엔터를 누르세요')
                clearConsole()
                continue  #contact가 비면 리스트 추가불가

            lst_contact.append(contact)
            input('연락처 추가 성공 \n 계속하려면 엔터를 누르세요')   #아무값도 안받지만 엔터 대기
            clearConsole()
        elif sel_menu == 2: #연락처 출력
            clearConsole()
            get_contact(lst_contact)
            input('계속하려면 엔터를 누르세요')   #아무값도 안받지만 엔터 대기
            clearConsole()
        elif sel_menu ==3 :
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            del_contact(lst_contact, name)
            input('연락처 삭제 성공 \n 계속하려면 엔터를 누르세요')
            clearConsole()
        elif sel_menu == 4:
            save_contact(lst_contact) # 파일DB저장
            break
        else:
            clearConsole()
        

# 주소록 입력함수
def set_contact():
    contact = None
    try:  #아무입력없이 엔터1 | 갯수 틀리면 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /))').split('/')
        contact = Contact(phone_num=phone_num, name=name, e_mail=e_mail, addr=addr)
    except Exception as e:
        print('입력갯수 확인(이름/핸드폰/이메일/주소)')
    finally:
        return contact #잘못되면 None 리턴, Contact 객체 리턴

# 주소록 전체출력
def get_contact(lst_contact):
    for contact in lst_contact:
        print(contact)

# 주소록 삭제
def del_contact(lst_contact, name):
    for i, contact in enumerate(lst_contact):
        if contact.name == name:
            del lst_contact[i]

# 주소록 파일DB 저장
def save_contact(lst_contact):
    f = open('./advanced/db_contact.txt', mode='w', encoding='utf-8')
    for contact in lst_contact:
        f.write(contact.name + '/') 
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')

    f.close()
 
# 주소록 파일DB 읽어오기
def load_contact(lst_contact:list):
    f = open('./advanced/db_contact.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line: break

        lines = line.rstrip('\n').split('/')  # 줄마지막 \n 제거하고, /로 나누고 나눈값을 리스트로
        if len(lines) != 4: continue   # 사이에 엔터공백있어도 출력 가능. 220506 엔터로 생기는
        contact = Contact(lines[0], lines[1],  lines[2],  lines[3])
        lst_contact.append(contact)

    f.close()


# 메뉴 출력 및 선택
def get_menu():
    str_menu = ('--주소록 프로그램 ver.1.1--\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)
    #0~9 숫자 외 ValueError 발생
    menu = 0   #초기화
    try:
        menu = int(input('메뉴입력 : '))
    except Exception as e:
        print(e)
    finally:
        return menu

def clearConsole() :
    command = 'clear' #mac,linux, unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'):
        command = 'cls' # windows, dos 화면 클리어 명령어
    os.system(command)

if __name__ == '__main__' :
    try:
        run()
    except KeyboardInterrupt as e:
        print('Ctrl+c 종료')
    
