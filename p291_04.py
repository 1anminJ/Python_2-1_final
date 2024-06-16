# 1
def hap(*nums):
    s = 0
    for num in nums:
        s += num
    return s
print(hap(1, 2, 3))
print(hap(*[1, 2, 3, 4]))

print('=' * 30)

# 2
def kwtest(**kwargs):
    a = 0
    for key in kwargs:
        if key in ['java', 'python']:
            a += kwargs[key]

    return a

print(kwtest(java=10, python=12, kotlin=36, c=8))
print(kwtest(**{'java': 10, 'python':5}))