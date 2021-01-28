import csv

def duqu_csv():
    csvshuju=[]
    with open('../date/aaa.csv','r',encoding='utf-8') as f:
        read = csv.reader(f)
        for line in read:
            # print(line)
            csvshuju.append(line)
        print(csvshuju)
    return csvshuju

duqu_csv()

