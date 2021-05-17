import tabula
import pandas as pd

df = tabula.read_pdf("table.pdf",pages ='1-125')


df.to_csv('2.csv')

df1 = pd.read_csv('2.csv')

