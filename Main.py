import pandas as pd
i = 0
while True:
    print('Gathering the dataset...')
    exec(open("MessageHandler.py").read())

    print('Processing...')
    print(pd._version)

    i += 1
    print('Number of gathered dataset ', i)
