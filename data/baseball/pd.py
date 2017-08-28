import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as sql

conn = sql.create_engine('mysql://dndd:dndddndd@localhost/csv')
df = pd.read_sql_table('pokemon')
df2 = pd.read_csv('hr.csv')
pd.set_option('display.width', 500)
pd.set_option('display.max_colwidth', 200)
#df2.to_csv('hr.csv')
