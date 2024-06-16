from datetime import date, timedelta

def getInput(prompt):
    while True:
        try:
            dateInput = input(prompt)
            year, month, day = dateInput.split('-') # '-'로 구분
            return date(int(year), int(month), int(day))
        except ValueError:
            print("형식이 올바르지 않습니다. 다시 시도하세요. (형식 : YYYY-MM-DD) ")

def untilXmas(input_date):
    xmasday = date(input_date.year, 12, 25)
    if input_date > xmasday:
        xmasday = date(input_date.year + 1, 12, 25)
    delta = xmasday - input_date
    return delta.days

def After100(input_date):
    date100 = timedelta(days=100)
    After100 = input_date + date100
    return After100

# 첫 번째 날짜 입력 받기
date1 = getInput("첫 번째 날짜를 입력하세요 (형식: YYYY-MM-DD): ")
print('%d년 %d월 %d일' % (date1.year, date1.month, date1.day))

# 첫 번째 날짜의 결과 계산 및 출력
xmas1 = untilXmas(date1)
after1001 = After100(date1)
print(f'크리스마스까지 남은 일수: {xmas1}')
print(f'100일 후: {after1001}')

# 두 번째 날짜 입력 받기
date2 = getInput("두 번째 날짜를 입력하세요 (형식: YYYY-MM-DD): ")
print('%d년 %d월 %d일' % (date2.year, date2.month, date2.day))

# 두 번째 날짜의 결과 계산 및 출력
xmas2 = untilXmas(date2)
after1002 = After100(date2)
print(f'크리스마스까지 남은 일수: {xmas2}')
print(f'100일 후: {after1002}')

# 날짜 입력 받기
# input_date = getInput("날짜를 입력하세요. (형식 : YYYY-MM-DD) : ")
# print('%d년 %d월 %d일' % (input_date.year, input_date.month, input_date.day))

# # 오늘부터 크리스마스까지 남은 일수 계산
# xmasday = date(input_date.year, 12, 25)
# if input_date > xmasday:
#     xmasday = date(input_date.year + 1, 12, 25)
# delta = xmasday - input_date
# print('크리스마스까지 남은 일수 : ', delta.days)
# today = date.today()
# print('%d년 %d월 %d일' % (today.year, today.month, today.day))
# xmasday = date(2024, 12, 25)
# delta = xmasday - today
# print(delta.days)

# # 오늘부터 100일 이후 날짜 출력
# date100 = timedelta(days=100)
# after100 = input_date + date100
# # after100 = today + date100
# print('100일 뒤 : ', after100)