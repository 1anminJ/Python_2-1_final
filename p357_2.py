import math
import statistics

if __name__ == '__main__':
    # 팩토리얼 계산
    print("1! =", math.factorial(1))
    print("6! =", math.factorial(6))
    print("11! =", math.factorial(11))
    print("16! =", math.factorial(16))

    # 주어진 리스트
    st = [80, 99, 77, 65, 92, 74, 82]

    # 리스트 출력
    print(f"\n{st}")

    # 통계 계산
    median = statistics.median(st)
    mean = statistics.mean(st)
    variance = statistics.variance(st)
    stdev = statistics.stdev(st)

    # 결과 출력
    print(f"중앙 값: {median:.2f}")
    print(f"평균: {mean:.2f}")
    print(f"분산: {variance:.2f}")
    print(f"표준편차: {stdev:.2f}")