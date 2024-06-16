from datetime import date, timedelta

def getInput(prompt):
    while True:
        try:
            dateInput = input(prompt)
            year, month, day = dateInput.split('-') # '-'로 구분
            return date(int(year), int(month), int(day))
        except ValueError:
            print("형식이 올바르지 않습니다. 다시 시도하세요. (형식 : YYYY-MM-DD) ")
# 날짜 입력 받기
input_date = getInput("날짜를 입력하세요. (형식 : YYYY-MM-DD) : ")
print('%d년 %d월 %d일' % (input_date.year, input_date.month, input_date.day))

# 오늘부터 크리스마스까지 남은 일수 계산
xmasday = date(input_date.year, 12, 25)
if input_date > xmasday:
    xmasday = date(input_date.year + 1, 12, 25)
delta = xmasday - input_date
print('크리스마스까지 남은 일수 : ', delta.days)
# today = date.today()
# print('%d년 %d월 %d일' % (today.year, today.month, today.day))
# xmasday = date(2024, 12, 25)
# delta = xmasday - today
# print(delta.days)

# 오늘부터 100일 이후 날짜 출력
date100 = timedelta(days=100)
after100 = input_date + date100
# after100 = today + date100
print('100일 뒤 : ', after100)