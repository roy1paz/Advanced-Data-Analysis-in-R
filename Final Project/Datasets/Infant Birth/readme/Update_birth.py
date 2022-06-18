import pandas as pd

Infant_Birth_DF = pd.read_csv('Natality, 2007-2020.csv')
Infant_Birth_DF = Infant_Birth_DF.iloc[0:6488]  # delete rows
del Infant_Birth_DF["Notes"]  # delete cols
Infant_Birth_DF.to_csv('Infant_Birth_2007-2020.csv')
