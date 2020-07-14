import PyPDF2  
import os
import re

directory = "../2020/pdfs"
errorFiles = []
for filename in os.listdir(directory):
# filename = "03-04-20_nldc_psp.pdf"
  # try:
    
    # creating a pdf file object  
    pdfFileObj = open("{}/{}".format(directory,filename), 'rb')    
    # creating a pdf reader object  
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)        
    # creating a page object  
    pageObj = pdfReader.getPage(0)  
    # extracting text from page  
    txt = pageObj.extractText()
    txtTrimmed = txt.rstrip()
    txtTrimmed = txtTrimmed.replace("\n", "")
    txtTrimmed = txtTrimmed.replace("," or ":" or "\'" or "_","")   
    # closing the pdf file object  
    pdfFileObj.close()
    ReportDate = re.search("[0-9][0-9]\.03\.2020", txtTrimmed)
    if ReportDate == None:
          newfilename = filename
    else:
          newfilename = ReportDate.group()
    os.rename("{}/{}".format(directory,filename),"{}/{}".format(directory,newfilename))
  # except:
  #   print("error with {}".format(filename))
  #   errorFiles.append(filename)
    print(newfilename)  

for error in errorFiles:
  f = open( '../2019/renameErrorFiles', 'w' )
  f.write( error )
  f.close()