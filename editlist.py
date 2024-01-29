
#apagando primeiro numero da lista
import pandas as pd

df = pd.read_csv('contact.csv')

df.to_csv('contact.csv', header=False)
df.to_csv('contact.csv', header=False, index=False)

