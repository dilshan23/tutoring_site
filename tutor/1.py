import tabula
import pandas as pd

df = tabula.read_pdf("1.pdf",pages ='1-125')


df.to_csv('2.csv')

df1 = pd.read_csv('2.csv')

