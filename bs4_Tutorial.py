import requests
from bs4 import BeautifulSoup
import json

url = "https://kloa.gg/characters"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
else:
    print("웹 페이지 로드 실패")
    exit()

soup = BeautifulSoup(html, "html.parser")

li = soup.find_all("li")
container = []

for div in li:
    obj = {}
    sub_obj = {}
    
    data = div.find_all("p")
    user_name = div.find_all("a")
    equip_row = div.find_all("div",class_="text-center")
    

    obj["user_name"] = user_name[0].get_text()
    obj["level"] = data[1].get_text()
    obj["class"] = data[2].get_text()
    obj["server"] = data[3].get_text()
    obj["guild"] = data[4].get_text() if data[4].get_text() else ""

    for element in equip_row:
        ela = element.find("p",class_="text-xs")
        # print(ela.get_text() if ela else "노 엘라")
        sub_obj["ela"] = ela.get_text() if ela else ""
        ark_passive = element.find_all("span")
        sub_obj["ark_evolution"] = ark_passive[0].get_text()
        sub_obj["ark_knowledge"] = ark_passive[1].get_text()
        sub_obj["ark_leap"] = ark_passive[2].get_text()
    # for equip in data[0]:
    
    obj["equip"] = sub_obj
    container.append(obj)
    # for string in test:
    #     anTest = string.get_text(strip=True)
    #     print(anTest)
                

    
    
# print(container)
    
    
    
    
    
    
        # testText = div.get_text(strip=True)
        # container.append(div.get_text(strip=True))


 