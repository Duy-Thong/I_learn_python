import csv
filepath=r"D://Learning//CodePTIT_Python//Python_Codeptit//Onthi//1.csv"
with open(filepath,'r',newline='',encoding='utf-8') as f:
    csvreader=csv.reader(f)
    header = next(csvreader, None)

    for row in csvreader:
        print(row[2])
