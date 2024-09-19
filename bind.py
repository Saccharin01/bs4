import os
import requests
from bs4 import BeautifulSoup

# 1. 메인 페이지 URL 설정
base_url = 'https://kr.ufc.com'
athletes_list_url = f'{base_url}/athletes/all'

# 2. 저장할 디렉토리 설정
images_dir = 'images'
html_dir = 'htmlStorage'

# 3. 디렉토리가 존재하지 않으면 생성
for directory in [images_dir, html_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# 4. 메인 페이지에서 데이터 크롤링
try:
    response = requests.get(athletes_list_url)
    response.raise_for_status()  # 요청이 성공했는지 확인
except requests.exceptions.RequestException as e:
    print(f"메인 페이지 요청 실패: {athletes_list_url}")
    print(e)
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

# 5. 'c-listing-athlete-flipcard__back' 클래스를 가진 div 요소 찾기
athlete_cards = soup.find_all('div', class_='c-listing-athlete-flipcard__back')

# 6. 각 선수의 이름과 이미지 추출 및 저장
for card in athlete_cards:
    # 6.1. 선수 이름 추출
    name_tag = card.find('span', class_='c-listing-athlete__name')
    if name_tag:
        # 선수 이름을 케밥 케이스로 변환 (소문자로 변환하고 띄어쓰기를 '-'로 치환)
        name = name_tag.get_text().strip().lower().replace(' ', '-')
        kebab_case_name = name

        # 6.2. 선수 이미지 추출 및 저장
        img_tag = card.find('img')
        if img_tag and "standing" in img_tag.get('src', ''):
            # 이미지 URL 추출
            img_url = requests.compat.urljoin(base_url, img_tag['src'])

            try:
                # 이미지 다운로드
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                # 이미지 파일 이름 및 경로 설정
                img_name = f"{kebab_case_name}.png"
                img_path = os.path.join(images_dir, img_name)

                # 이미지 파일 저장
                with open(img_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"이미지 저장됨: {img_path}")
            except requests.exceptions.RequestException as e:
                print(f"이미지 다운로드 실패: {img_url}")
                print(e)

        # 6.3. 선수 상세 페이지 URL 생성 및 HTML 저장
        athlete_url = f'{base_url}/athlete/{kebab_case_name}'
        try:
            # 선수 상세 페이지 요청
            athlete_response = requests.get(athlete_url)
            athlete_response.raise_for_status()  # 요청이 성공했는지 확인

            # HTML 파일 이름 및 경로 설정
            html_name = f"{kebab_case_name}.html"
            html_path = os.path.join(html_dir, html_name)

            # HTML 파일 저장
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(athlete_response.text)

            print(f"선수 페이지 저장됨: {html_path}")
        except requests.exceptions.HTTPError as e:
            print(f"선수 페이지 불러오기 실패: {athlete_url}")
            print(e)
        except requests.exceptions.RequestException as e:
            print(f"선수 페이지 요청 중 오류 발생: {athlete_url}")
            print(e)
