# def zodiac():
#     import requests
#     from bs4 import BeautifulSoup
#     url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%8F%BC%EC%A7%80%EB%9D%A0%20%EC%9A%B4%EC%84%B8"
#     #<p class="text _cs_fortune_text">
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, "html.parser") #beautifulsoup은 정리하는 도구, req.text는 재료, html.parser는 정리 방식
#     txt = soup.find("p", attrs= {"class", "text _cs_fortune_text"}).get_text() #p 태그이면서 특정 속성, 속성값을 가진 p를 찾는다. get_text는 글자들만 뽑아준다
#     print(txt)
#
# zodiac()