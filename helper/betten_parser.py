import pandas as pd


#lstdates = list(pd.date_range(start="2020-06-12",end="2020-07-01").values.astype('<M8[D]').astype(str))


while True:
    from data_prep import save     
    import datetime
    save()
    today = str(datetime.date.today())
    lstdates = [today]
    n0 = 5000
    for date in lstdates:
        t = 0 
        for n in range(n0,10000):
            for k in range(9,15):
                if n%10 ==0:
                    print(n,k,today)
                k = "{0:02d}".format(k)
                try:
                    url = 'https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv/divi-intensivregister-{}-{}-15/viewdocument/{}'.format(date,k,n)
                    data = pd.read_csv(url)
                    data.to_csv('../data/beds_DE_{}.csv'.format(date),index=False)
                    t = 1
                except:
                    if t ==1:
                        print(url) 
                        #print(n)
                        break
                    pass
