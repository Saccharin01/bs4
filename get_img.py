import os
import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지의 URL 설정
url = 'https://kr.ufc.com/athletes/all'

# 2. 웹 페이지 가져오기
response = requests.get(url)

# 3. BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 4. 'c-listing-athlete-flipcard__back' 클래스를 가진 div 요소 찾기
athlete_cards = soup.find_all('div', class_='c-listing-athlete-flipcard__back')

# 5. 저장할 디렉토리 설정
save_dir = 'images'

# 6. 디렉토리가 존재하지 않으면 생성
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 7. 각 선수의 이름과 이미지 추출 및 저장
for card in athlete_cards:
    # 2. 'c-listing-athlete__name' 클래스를 가진 span 태그에서 선수 이름 추출
    name_tag = card.find('span', class_='c-listing-athlete__name')
    if name_tag:
        # 선수 이름을 케밥 케이스로 변환 (소문자로 변환하고 띄어쓰기를 '-'로 치환)
        name = name_tag.get_text().strip().lower().replace(' ', '-')
        kebab_case_name = name

        # 3. 'img' 태그의 src 속성 중에 'standing'이 포함된 이미지 추출
        img_tag = card.find('img')
        if img_tag and "standing" in img_tag.get('src', ''):
            # 이미지 URL 추출
            img_url = requests.compat.urljoin(url, img_tag['src'])

            # 이미지 다운로드
            img_data = requests.get(img_url).content

            # 4. 파일 이름 설정 (선수 이름을 기반으로 한 파일명)
            img_name = f"{kebab_case_name}.png"
            
            # 파일 경로 생성 (디렉토리 경로와 파일명을 결합)
            img_path = os.path.join(save_dir, img_name)

            # 이미지 파일을 지정한 디렉토리에 저장
            with open(img_path, 'wb') as f:
                f.write(img_data)

            print(f"이미지 저장됨: {img_path}")
