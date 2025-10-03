import pandas as pd
import re

input_file_path = "input/school_code.csv"
output_file_path = "output/school_name.csv"
lst = []
high_school = pd.DataFrame()

with open(input_file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.split(",")
        if "神奈川" in line[2]:
            if "高校" in line[1]:
                lst.append(line[0:7+1])

# print(lst)
high_school = pd.DataFrame(lst, columns=["学校コード", "学校種", "都道府県番号", "設置区分", "本分校", "学校名", "学校所在地", "郵便番号"])
print(high_school)

high_school.to_csv(output_file_path, index=False, encoding="utf-8")
print("finish")