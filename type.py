


user_input = input("입력 해주세요 : ")



try :
  test = int(user_input)
  print("입력하신 내용은 숫자형 입니다.")
    
except ValueError:
  try:
    test = float(user_input)
    print("입력하신 내용은 소수점이 있는 숫자입니다.")
  
  except ValueError:
    test = str(user_input)
    print("입력하신 내용은 문자열 입니다.")











#   print(user_input)

# if type(user_input) is str:
#   print("입력하신 내용은 문자열 입니다.")

# elif type(user_input) is int:
#   print("입력하신 내용은 int 입니다")
