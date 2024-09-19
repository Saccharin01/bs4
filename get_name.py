import requests
from bs4 import BeautifulSoup
import os

# 1. baseURL 설정
base_url = 'https://kr.ufc.com/athletes/all'
dir_name = 'htmlStorage'

requestURL = os.path.join(base_url,"/all")
# 디렉토리가 존재하지 않으면 생성
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

# 2. 페이지에서 데이터 크롤링
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 'c-listing-athlete__name' 클래스를 가진 span 태그 검색
athlete_names = soup.find_all('span', class_='c-listing-athlete__name')


# 4. 각 선수의 이름을 케밥 케이스로 변환 후 엔드포인트로 활용하여 크롤링
for athlete in athlete_names:
    name = athlete.get_text().strip().lower()  # 이름을 소문자로 변환
    kebab_case_name = name.replace(' ', '-')   # 띄어쓰기를 '-'로 변환하여 케밥 케이스 생성

    # 5. 새로운 엔드포인트 URL 생성
    athlete_url = f'https://kr.ufc.com/athlete/{kebab_case_name}'
    
    try:
        # 6. 각 선수의 페이지 데이터를 가져옴
        athlete_response = requests.get(athlete_url)
        athlete_response.raise_for_status()  # 200 OK 아닌 경우 예외 발생
        
        # 7. 데이터를 파일로 저장
        file_name = f"{kebab_case_name}.html"
        path = os.path.join(dir_name, file_name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(athlete_response.text)
        
        print(f"선수 페이지 저장됨: {file_name}")
        
    except requests.exceptions.HTTPError as e:
        print(f"선수 페이지 불러오기 실패: {athlete_url}")
        print(e)

