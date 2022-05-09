# 주소록 프로그램 ver.1.2
# 작성일 : 2022-05-09
# 작성자 : SEONG HG
# 설  명 : 월요일~ 파일 DB에서 Oracle로 변경.
import os
import cx_Oracle as ora

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

def initDB():
    dsn = ora.makedsn('localhost', 1521, service_name='orcl')
    conn = ora.connect(user='scott', password='tiger', dsn=dsn, encoding='utf-8')
    return conn

def run():    
    conn = initDB()   #oracle 연결해서 연결객체 생성
    clearConsole()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:
            clearConsole()
            isval = set_contact(conn)
            if isval:
                input('연락처 추가 성공 \n 계속하려면 엔터를 누르세요')   #아무값도 안받지만 엔터 대기
            else:
                input('오류발생! 관리자 문의 요망')

            clearConsole()
        elif sel_menu == 2: #연락처 출력
            clearConsole()
            get_contact(conn)
            input('계속하려면 엔터를 누르세요')   #아무값도 안받지만 엔터 대기
            clearConsole()
        elif sel_menu == 3 :
            clearConsole()
            name = input('삭제할 이름 입력 > ')
            del_contact(conn, name)
            input('연락처 삭제 성공 \n 계속하려면 엔터를 누르세요')
            clearConsole()
        elif sel_menu == 4:
            conn.close()
            break
        else:
            clearConsole()
        
# 주소록 입력함수
def set_contact(conn):
    contact = None
    isSucceed = False # 입력 성공여부
    try:  #아무입력없이 엔터1 | 갯수 틀리면 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /))').split('/')
        contact = Contact(phone_num=phone_num, name=name, e_mail=e_mail, addr=addr)
        # DB 처리
        cur = conn.cursor()
        query = ('INSERT INTO addressbook '   # addressbook과 ' 사이 공백 꼭 필요. 없으면 뒤에 VALUES랑 한 단어돼서 오류 
                'VALUES (SEQ_ADDRBOOK.nextval, :1, :2, :3, :4)')
        tup = (contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close()
        isSucceed = True
    except Exception as e:
        print('입력갯수 확인(이름/핸드폰/이메일/주소)')
        isSucceed = False 
    finally:
        return isSucceed  # True면 DB입력성공, False면 DB입력실패

# 주소록 전체출력
def get_contact(conn):
    cur = conn.cursor()
    query = 'SELECT name, phone_num, e_mail, addr FROM addressbook'

    for row in cur.execute(query):
        contact = Contact(row[0], row[1], row[2], row[3])
        print(contact)
    
    cur.close()

# 주소록 삭제
def del_contact(conn, name):
    cur= conn.cursor()
    query = f"DELETE FROM addressbook WHERE name = '{name}'"
    cur.execute(query)
    conn.commit()
    cur.close()

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
    
