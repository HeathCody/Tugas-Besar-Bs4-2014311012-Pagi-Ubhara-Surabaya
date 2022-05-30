from bs4 import BeautifulSoup, NavigableString
import requests

url  = "https://www.wavsource.com/people/famous.htm"

get = requests.get(url, headers={"User-Agent": "XY"})
# print(get.status_code) 
# Kode status_code akan menghasilkan output "200" yang berarti halaman tersebut memberikan respon 200 OK dan dapat kita lakukan scraping.

bs = BeautifulSoup(get.text, 'html.parser')
invalid_tags = ['b', 'i', 'u', 'a']
main = bs.find_all('td', class_='c22')
# for tag in invalid_tags:
#     for suara in main:
#         wav = suara.find('p')
#         print (wav)
for paragraf in bs.find_all("p"):
    print(paragraf.get_text().strip())
