
import csv

with open('markets.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    count = 0

    for row in reader:
        # print(row)

        if row['Symbol'] == "ORCL":
            print(row['Name'])

        if "Microsoft" in row['Name']:
            print(row['Name'] + " - " + row['Symbol'])

        # if count > 1000:
        #     break

        # count += 1

# print(reader)