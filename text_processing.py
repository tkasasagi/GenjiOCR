import pandas as pd

dataframe = pd.read_csv('20000.csv',header = None)

vol_list  = []
page_list = []
line_list = []
text_list = []

vol = ''
page = ''
line = ''
text = ''

def change_zen(x):
    han_char = ''
    zen_char  = ['０','１','２','３','４','５','６','７','８','９','Ｖ','Ｐ','Ｌ']
    for i in range(len(x)):
        if (zen_char.index(x[i]) == 10):
            han_char += 'V'
        elif (zen_char.index(x[i]) == 11):
            han_char += 'P'
        elif (zen_char.index(x[i]) == 12):
            han_char += 'L'
        else:
            han_char += str(zen_char.index(x[i]))
        
    return han_char
        

for i in range(len(dataframe)):  
    #Get Volume number    
    if (dataframe.iloc[i,0][0:1] == 'Ｖ'):
        #print(dataframe.iloc[i,0])  
        vol = change_zen(dataframe.iloc[i,0][0:3])
    vol_list.append(vol)
    
    #Get Page Number
    if (dataframe.iloc[i,0][0:1] == 'Ｐ'):
        #print(dataframe.iloc[i,0])  
        page = change_zen(dataframe.iloc[i,0][0:4])
    page_list.append(page)
    
    #Get Line Number
    if (dataframe.iloc[i,0][0:1] == 'Ｌ'):
        #print(dataframe.iloc[i,0])  
        line = change_zen(dataframe.iloc[i,0][0:3])
        line_list.append(line)
        text = dataframe.iloc[i, 0][3:]
        text_list.append(text)
    else:
        line_list.append('0')
        text_list.append('0')

savedata = pd.DataFrame()
savedata['vol'] = vol_list
savedata['page'] = page_list
savedata['line'] = line_list
savedata['text'] = text_list

savedata = savedata[savedata['line'] != '0']

#Save back to CSV
savedata.to_csv('text.csv', index = False)


