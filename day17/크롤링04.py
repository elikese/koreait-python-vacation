import requests
from bs4 import BeautifulSoup

# 도전) 아래 url 게시판의 제목들만 추출해서 출력!
url = "https://de.mofa.go.kr/de-ko/brd/m_7204/list.do"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

trs = soup.select("#contents > div.board_list > table > tbody > tr")
for tr in trs:
    # select는 언제나 리스트를 리턴
    # [태그1, 태그2...]
    # 담는 "순서"가 위에서 부터 아래로 담음
    title_tag = tr.select(".al div a")[0]
    title = title_tag.text

    candidate = tr.select("td div")

    date_tag = candidate[-1] # 맨뒤에 담긴것
    date = date_tag.text
    author_tag = candidate[-2] # 맨뒤 바로앞에 담긴것
    author = author_tag.text

    print(f"{author}: {title[:10]}... {date}")



# 게시글 제목 말고
# 실제 게시글 내용 여러개를 크롤링
# -> url 패턴파악 먼저

# 2975116&page=1 첫번째
# 2975115&page=1 두번째
# 2975107&page=1 마지막

BASE_ID = 2975116
BASE_URL = "https://de.mofa.go.kr/de-ko/brd/m_7204/view.do?seq="
target_urls = []
for num in range(0, 10):
    print(f"{BASE_URL}{BASE_ID - num}&page=1")
    target_urls.append(f"{BASE_URL}{BASE_ID - num}&page=1")

for url in target_urls:
    response = requests.get(url)

    # 통신성공 코드
    # 200이면 통신은 성공한것
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")








