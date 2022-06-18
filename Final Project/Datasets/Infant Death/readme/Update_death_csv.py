import pandas as pd

Infant_Death_DF = pd.read_csv('Linked Birth  Infant Death Records, 2007-2019.csv')
Infant_Death_DF = Infant_Death_DF.iloc[0:6818]  # delete rows
del Infant_Death_DF["Notes"]  # delete cols
Infant_Death_DF.to_csv('Infant_Death_2007-2019.csv')
