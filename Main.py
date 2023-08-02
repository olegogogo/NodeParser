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
print(df)

# finally save to csv
df.to_csv('output.csv', header=False, index=False)