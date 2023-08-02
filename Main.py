import pandas as pd
'''i = 0
while True:
    print('Gathering the dataset...')
    exec(open("MessageHandler.py").read())

    print('Processing...')
    print(pd._version)

    i += 1
    print('Number of gathered dataset ', i)
'''
columnnames = ['Date', 'Node id', 'Uptime', 'Health']
df = pd.read_csv('temp_output.csv', delimiter=';', names=columnnames)

listid = list(df['Node id'].unique())

finalDF = pd.DataFrame()
for i in listid:
    finalDF = finalDF._append(pd.DataFrame(data=[[df['Date'][df['Node id']==i].iloc[-1],
                                                  i,
                                                  df['Uptime'][df['Node id']==i].iloc[-1],
                                                  df['Health'][df['Node id']==i].mean()]]))

# finally save to csv
finalDF.to_csv('output.csv', header=False, index=False)