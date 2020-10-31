import pandas as pd
import os

def importcsv(a):
    return pd.read_csv(a, parse_dates=['daten_stand'])
betten_data = os.listdir('../data')

bettenlst = []
for n in sorted(betten_data):
    if n.endswith('.csv'):
        if n != 'gesamt.csv':
            bettenlst.append(importcsv('../data/{}'.format(n)))
        else:
            pass
df = pd.concat(bettenlst)

df.to_csv('../data/gesamt.csv')