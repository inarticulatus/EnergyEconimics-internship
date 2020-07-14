# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import pdfplumber
import csv
directory = "~/Academics/internship"
filename = "26.05.2020"
pdf = pdfplumber.open("/home/utkarsh/Academics/internship/26.05.2020")

p1 = pdf.pages[1]
image = p1.to_image()
image.reset().debug_tablefinder()


# %%
crop = p1.within_bbox((10, 200, p1.width, p1.height-300))
cropIm = crop.to_image()
cropIm.reset().debug_tablefinder()


# %%
table = crop.extract_table()
df = pd.DataFrame(table[1:], columns=table[0])
df = df.drop(["Region"], axis = 1)
df.to_csv("/home/utkarsh/Academics/csv/{}".format(filename))


# %%
p1.width


# %%
df


# %%
import pandas as pd
import pdfplumber
import csv
import os
directory = "/home/utkarsh/Academics/csv"
filename = "26.03.2020"
# for filename in os.listdir(directory):
print(filename)
df = pd.read_csv("{}/{}".format(directory,filename), index_col=0)
print(df.info)
df.drop([1],axis=0)
print("\n"*2)
# df.to_csv("/home/utkarsh/Academics/csv/{}".format(filename))

