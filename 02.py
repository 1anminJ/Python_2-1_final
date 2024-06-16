# import random
#
# # 1에서 99까지의 난수 10개 생성
# random_list = [random.randint(1, 99) for i in range(10)]
#
# # 리스트 정렬
# sorted_list = sorted(random_list)
#
# # 리스트 역순 정렬
# reversed_list = sorted_list[::-1]
#
# # 결과 출력
# print("Original list:", random_list)
# print("Sorted list:", sorted_list)
# print("Reversed list:", reversed_list)


import random

# 1에서 99까지의 난수 10개 생성
random_list = [random.randint(1, 99) for _ in range(10)]

# 1의 자리 숫자로 정렬
sorted_list = sorted(random_list, key=lambda x: x % 10)

# 리스트 역순 정렬
reversed_list = sorted_list[::-1]

# 결과 출력
print("Original list:", random_list)
print("Sorted by unit digit:", sorted_list)
print("Reversed list:", reversed_list)
