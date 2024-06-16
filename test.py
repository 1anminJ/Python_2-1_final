import random

# 1에서 100 사이의 섭씨 온도 9개를 난수로 생성
cel = [random.randint(1, 100) for i in range(9)]

# 섭씨 온도 리스트 정렬
sorted_cel = sorted(cel)
print('섭씨 온도 : ', sorted_cel)

# 섭씨를 화씨로 변환하는 람다 함수
c_to_fahrenheit = lambda cels: cels * 9/5 + 32

# map 함수를 사용해 화씨 온도 리스트 생성
fah = list(map(c_to_fahrenheit, sorted_cel))
print('화씨 온도 : ', fah)

# 섭씨와 화씨 온도를 출력
for celsius, fahrenheit in zip(sorted_cel, fah):
    print(f"섭씨 온도 {celsius} => 화씨 {fahrenheit:.2f}")