# 함수 연습

def A(x) :
    print(x)

A('안녕')
A('Hi')

def B(a, b) :
    print(a + b)

B(3, 4)
B(7, 10)

def print_with_smile (str) :
    print(str + ":D")
print_with_smile("안녕하세요")

def print_upper_price(num):
    print(num * 1.3)
print_upper_price(50)

def print_sum(a, b):
    print(a + b)
print_sum(5,7)

def print_max(a, b, c):
    max_val = 0
    if a > max_val :
        max_val = a 
    if b > max_val :
        max_val = b
    if c> max_val :
        max_val = c
    print(max_val)

print_max(4,5,6)
