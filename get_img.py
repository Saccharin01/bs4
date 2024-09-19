import os
import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지의 URL 설정
url = 'https://kr.ufc.com/athletes/all'

# 2. 웹 페이지 가져오기
response = requests.get(url)

# 3. BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 4. 모든 img 태그 찾기
images = soup.find_all('img')

# 5. 저장할 디렉토리 설정
save_dir = 'images'

# 6. 디렉토리가 존재하지 않으면 생성
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 7. 특정 문자열("standing")을 포함한 img 태그의 src 추출 및 이미지 저장
i = 0  # 파일 이름을 위한 카운터 초기화

for img in images:
    src = img.get('src')
    
    # src에 "standing" 문자열이 있는지 확인
    if "standing" in src:
        # 절대 경로로 변환
        img_url = requests.compat.urljoin(url, src)
        
        # 이미지 다운로드
        img_data = requests.get(img_url).content
        
        # 파일 이름 설정 (숫자로 된 파일명 생성)
        img_name = f"image_{i}.png"
        
        # 파일 경로 생성 (디렉토리 경로와 파일명을 결합)
        img_path = os.path.join(save_dir, img_name)
        
        # 이미지 파일을 지정한 디렉토리에 저장
        with open(img_path, 'wb') as f:
            f.write(img_data)
        
        print(f"이미지 저장됨: {img_path}")
        
        # 카운터 증가
        i += 1