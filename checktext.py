import pandas as pd

text = pd.read_csv("text_data.csv", header = None)

text.head()

text[3][1]


count = 0
page = "P001"

for i in range(len(text)):
    if (len(text[3][i]) < 15 and text[1][i] != page):
        print(i)
        page = text[1][i]
        count += 1
        
print(count)
    