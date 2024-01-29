#with open("mensagem.txt") as msg_text:
 #  msg_text2 = msg_text.read()
   #print(msg_text2)

import csv
import pandas as pd

with open("contact.csv", "r") as arquivo_csv:
    arquivo_csv = csv.reader(arquivo_csv) 
    toplinha = next(arquivo_csv)
    toplinha_var1 = "".join(map(str,toplinha))
    toplinha('contact.csv', header=False)
    toplinha('contact.csv', header=False, index=False)


    print(toplinha_var1)

