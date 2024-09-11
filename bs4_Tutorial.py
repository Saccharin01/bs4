import requests
from bs4 import BeautifulSoup

url = "https://kloa.gg/"
response = requests.get(url)

if response.status_code == 200:
  html = response.text
else:
  print("웹 페이지 로드 실패")
  exit()
  
soup = BeautifulSoup(html, "html.parser")

with open("test.html","w",encoding="utf-8")as file:
  try:
    file.write(soup.prettify())
  except:
    print("파일 작성에 실패했습니다.")