import pandas as pd
from urllib.parse import quote

# 「https://ja.wikipedia.org/wiki/高校名」みたいになってる
# https://ja.wikipedia.org/wiki/

school_name = pd.read_csv("output/school_name.csv", encoding="utf-8")
for name in school_name["学校名"]:
    print(f"https://ja.wikipedia.org/wiki/{name}") # urllib.parse.quote()でへんかんするらしい
    print(f"https://ja.wikipedia.org/wiki/{quote(name)}") # なんかある程度はwikipediaが補正してくれてる？