import basicData

count = 0

def process_dict(d):
    global count
    for key, value in d.items():
        if "교통" in key:
            if isinstance(value, dict):
                # 값이 딕셔너리인 경우, 재귀적으로 처리
                process_dict(value)
            else:
                # 값이 숫자일 경우, count에 추가
                if isinstance(value, (int, float)):
                    count += value

# 모든 딕셔너리 처리
for item in basicData.basic_data:
    if isinstance(item, dict):
        process_dict(item)


print("최종 count 값:", count)