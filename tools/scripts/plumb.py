import pandas as pd
import pdfplumber
import csv
import os
directory = "../2020/pdfs"
# filename = "14.03.2020"
exceptionFiles = []
for filename in os.listdir(directory):
    pdf = pdfplumber.open("{}/{}".format(directory,filename))
    print(filename)
    p1 = pdf.pages[1]
    print(p1.width)
    try:
        if p1.width < 1000:
            crop = p1.within_bbox((10, 180, p1.width, p1.height-310))
            im = crop.to_image()
            table = crop.extract_table()
        else:
            im = p1.to_image()
            table = p1.extract_table()
        df = pd.DataFrame(table[1:], columns=table[0])
        df = df.drop(["Region"], axis = 1)  
    except:
        exceptionFiles.append(filename)
        
    
    df.to_csv("../2020/csv/{}".format(filename))
    pdf.close()
print(exceptionFiles)        