import pandas as pd
lstdates = list(pd.date_range(start="2020-06-12",end="2020-07-01").values.astype('<M8[D]').astype(str))
#lstdates = ['2020-09-14']
lstbetten=[]

n0 = 3500
for date in lstdates:
    t = 0 
    for n in range(n0,10000):
        if n%10 ==0:
            print(n)
        try:
            url = 'https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv/divi-intensivregister-{}-12-15-2/viewdocument/{}'.format(date,n)
            data = pd.read_csv(url)
            data.to_csv('betten_data/beds_DE_{}.csv'.format(date),index=False)
            t = 1
        except:
            if t ==1:
                print(url) 
                #print(n)
                break
            pass