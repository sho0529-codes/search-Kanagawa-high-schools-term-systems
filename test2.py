import pandas as pd
from urllib.parse import quote

# 「https://ja.wikipedia.org/wiki/高校名」みたいになってる
# https://ja.wikipedia.org/wiki/

input_file = "output/school_name.csv"
output_file= "output/school_url.csv"

school_name = pd.read_csv(input_file, encoding="utf-8")
with open(output_file, "w", encoding="utf-8") as f:
    for name in school_name["学校名"]:
        # print(f"https://ja.wikipedia.org/wiki/{name}") # urllib.parse.quote()でへんかんするらしい
        # print(f"https://ja.wikipedia.org/wiki/{quote(name)}") # なんかある程度はwikipediaが補正してくれてる？
        f.write(f"{name}：https://ja.wikipedia.org/wiki/{quote(name)}\n")
print("finish")