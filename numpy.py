import basicData
import tutorial
# count = 0

# def process_dict(d):
#     global count
#     for key, value in d.items():
#         if "교통" in key:
#             if isinstance(value, dict):
#                 # 값이 딕셔너리인 경우, 재귀적으로 처리
#                 process_dict(value)
#             else:
#                 # 값이 숫자일 경우, count에 추가
#                 if isinstance(value, (int, float)):
#                     count += value

# # 모든 딕셔너리 처리
# for item in basicData.basic_data:
#     if isinstance(item, dict):
#         process_dict(item)


# print("최종 count 값:", count)



count = 0
container = []

def recursionDef(data):
    
    global container
    global count
    
    for element in data:
        if type(element) == list:
            recursionDef(element)
        elif type(element) == dict :
            for key, value in element.items():
                if "교통" in key and type(value) == int or type(value)==float:
                    container.append(key)
                    count += value
                if type(value) == dict or type(value) == list:
                    recursionDef(value)

                            

recursionDef(tutorial.tutorial)

print(container)
print(count)
print(len(container))