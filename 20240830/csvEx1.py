import csv

f = open('test.csv', 'r', encoding='EUC-KR')

dataHeader = csv.reader(f)
header = next(dataHeader)
print(header)

data = csv.reader(f, delimiter=',')
for row in data :
    print(row)

f.close()