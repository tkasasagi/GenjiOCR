import pandas as pd

text = pd.read_csv("text_data.csv", header = None)

text.head()

text[3][3]

count = 0
page = ""
filelist = []
filecut = ""
cutlength = 12

for i in range(len(text)):
    if (len(text[3][i]) < cutlength and text[1][i] != page):
        filecut = text[0][i][1:] + "_" + text[1][i][1:]
        filelist.append(filecut)
        print(filecut)
        page = text[1][i]
        count +=1
        
print(count)

