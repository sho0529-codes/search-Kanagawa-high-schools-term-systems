# これ（https://qiita.com/Octoparse_Japan/items/902f336d1b328eb38dbf）参考にする
# なにかエラーでwikipediaに入れないっぽい？（Please set a user-agent and respect our robot policy https://w.wiki/4wJS. See also T400119.）たぶん何かしらのセキュリティに引っかかってる

import requests
from bs4 import BeautifulSoup

# 解析するWebサイトのURL
# url = "https://example.com"  # 解析したいURL
url = "https://ja.wikipedia.org/wiki/%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C%E7%AB%8B%E9%B6%B4%E8%A6%8B%E9%AB%98%E7%AD%89%E5%AD%A6%E6%A0%A1"

# HTMLを取得
response = requests.get(url)

# BeautifulSoupで解析
soup = BeautifulSoup(response.content, "html.parser")

# HTML全体を出力
print(soup.prettify())
