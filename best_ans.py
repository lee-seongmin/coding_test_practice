import time

# 딕셔너리 데이터 생성 (1부터 100,000까지 숫자를 키와 값으로 가지는 딕셔너리)
dic = {chr(65 + (i % 26)) + str(i): i for i in range(1, 100001)}

# 첫 번째 방법: for문 활용
start_time = time.time()  # 시작 시간 측정
rev = dict()
for key, value in dic.items():
    rev[value] = key
end_time = time.time()  # 끝 시간 측정
print(f"for문 실행 시간: {end_time - start_time:.10f} 초")

# 두 번째 방법: map 및 lambda 활용
start_time = time.time()  # 시작 시간 측정
rev_map = dict(map(lambda t: (t[1], t[0]), dic.items()))
end_time = time.time()  # 끝 시간 측정
print(f"map 및 lambda 실행 시간: {end_time - start_time:.10f} 초")