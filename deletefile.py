import os

directory = "column5/"
filelist = os.listdir(directory)

for i in filelist:
    if (i[-6:-5] != "_" and int(i[-6:-4]) > 11):
        #print("remove file" , i)
        os.remove(directory + i)


#Delete blank images
        
im = i