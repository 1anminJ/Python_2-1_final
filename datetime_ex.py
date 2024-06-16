from datetime import date

# 오늘부터 크리스마스까지 남은 일수 계산
today = date.today()
print('%d년 %d월 %d일' % (today.year, today.month, today.day))

xmasday = date(2024, 12, 25)
delta = xmasday - today
print(delta.days)

from datetime import timedelta

# 오늘부터 100일 이후 날짜 출력
date100 = timedelta(days=100)
after100 = today + date100
print(after100)