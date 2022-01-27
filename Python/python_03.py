# def 함수명("매개변수"):
#     실행할 문장

def my_sum_func(a,b):
    result = a+b
    return result

my_sum = my_sum_func(10,20)
print(my_sum)

class myBakery:
    title = ''
    time = ''
    taste = ''

cookie = myBakery()
cookie.title = '머핀'
cookie.time = '1h'
cookie.taste = '초콜릿'

print(cookie)
print(cookie.title)
print(cookie.time)
print(cookie.taste)