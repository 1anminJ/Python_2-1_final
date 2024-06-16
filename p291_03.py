# 1번
def test1():
    print('\t', a * 1)

a = 1
test1()
print(a)

print('=' * 50)

# 2번
def test2():
    b = 11
    print('\t', b * 1)
b = 1
test2()
print(b)

print('=' * 50)

# 3번
def test3():
    global c
    c = 10
    print('\t', c * 1)
c = 1
test3()
print(c)

print('=' * 50)

# 4번
def test4():
    d = 10
    e = d + 10
    print('\t', e)
e = 1
test4()
print(e)