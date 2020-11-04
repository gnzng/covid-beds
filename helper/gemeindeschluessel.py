import PyPDF2
import numpy as np
import pandas as pd


'''
pdfFileObj = open('Liste-Amtlicher-Gemeindeschluessel-AGS-2015.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
seite1 = pdfReader.getPage(0).extractText()

glst = []
f = seite1[432:].split('\n')
for n in range(len(f)):
    if f[n] != '':
        if len(f[n])<=25:
            glst.append(f[n])

for p in range(1,209):
    seitex = pdfReader.getPage(p).extractText()
    g = seitex[:].split('\n')
    for n in range(len(g)):
        if g[n] != '':
            if len(g[n])<=90:
                glst.append(g[n])

glst = np.array(glst).reshape(int(len(glst)/4),4)

t = pd.DataFrame(glst,columns=['Stadt/Gemeinde','Verwaltungseinheit','Gemeindeschlüssel','Bundesland'])
#print(t['Gemeindeschlüssel'][3])

t.to_csv('schluessel.csv',index=False)

'''

t = pd.read_csv('schluessel.csv')
t['Bundesland'] = t['Bundesland'].replace('Thüringen€','Thüringen')

t['Gemeinde+Bundesland'] = t['Stadt/Gemeinde'] + ', '+ t['Bundesland']
t['5stellig'] = t['Gemeindeschlüssel']/1000
t['5stellig'] = t['5stellig'].round(decimals=0).astype(int)

print(t['Bundesland'].head(30))

s = t.groupby('5stellig')['Stadt/Gemeinde'].apply(lambda x: "{%s}" % ', '.join(x))
s = t.groupby('5stellig').agg(Gemeinden=('Stadt/Gemeinde', ', '.join)).reset_index()

t.to_csv('alles.csv')

p = pd.read_csv('kreise.csv')

def zahl2gemeinde(a):
    return str(p[p['5stellig'] == a]['Gemeinden'].iat[0])


#print(zahl2gemeinde(5754))

#print(t.head())

#print(list(t['Verwaltungseinheit']).count('Gemeindefreies Gebiet'))

lst1 = []
lst2 = []
for n in range(int(len(t))):
    if str(t['Gemeindeschlüssel'][n])[:-3] not in lst1:
        #print(t['Gemeindeschlüssel'][n][:-3])
        lst1.append(str(t['Gemeindeschlüssel'][n])[:-3])
        #f = t.iloc[[n]]
        #lst2.append(f[:].values)

#print(len(lst1))

t = t.set_index('Gemeindeschlüssel')
#t['Gemeindeschlüssel'].astype(str)
t = t.filter(like='0000',axis=0)
#print(len(t))



tt = pd.read_csv('../data/beds_DE_2020-11-02.csv')

#print(pd.DataFrame(list(set(tt['gemeindeschluessel'].astype(str)) & set(test))).filter(like='1001'))
