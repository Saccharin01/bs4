def save_image(img_url, img_name):
    try:
        img_response = requests.get(img_url)
        img_response.raise_for_status()
        
        img_path = os.path.join(images_dir, img_name)
        with open(img_path, 'wb') as f:
            f.write(img_response.content)
        
        print(f"이미지 저장됨: {img_path}")
        return img_path
    except requests.exceptions.RequestException as e:
        print(f"이미지 다운로드 실패: {img_url}\n{e}")
        return None
