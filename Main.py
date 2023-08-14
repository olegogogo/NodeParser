import pandas as pd
import datetime

columnnames = ['Date', 'Node id', 'Uptime', 'Health']
finalDF = pd.DataFrame()

while True:
    try:
        print('Listening nodes... : ', (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%H:%M:%S"))
        exec(open("MessageHandler.py").read())

        df = pd.read_csv('temp_output.csv', delimiter=';', names=columnnames)

        listid = list(df['Node id'].unique())

        for i in listid:
            finalDF = finalDF._append(pd.DataFrame(data=[[df['Date'][df['Node id']==i].iloc[-1],
                                                          i,
                                                          df['Uptime'][df['Node id']==i].iloc[-1],
                                                          df['Health'][df['Node id']==i].mean()]]))

        # finally save to csv
        finalDF.to_csv('output.csv', header=False, index=False)

    except Exception:
        pass