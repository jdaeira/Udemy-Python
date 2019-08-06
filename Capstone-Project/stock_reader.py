
import csv

with open('stock_tickers.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    count = 0

    for row in reader:
        #print(row['Ticker'] + " - " +  row['Name'])

        if row['Ticker'] == "ORCL":
            print(row['Name'])

        # if count > 1000:
        #     break

        # count += 1

# print(reader)