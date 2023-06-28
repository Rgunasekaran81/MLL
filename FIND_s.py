import csv

def getdata(filename):
    data = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
            data.append(r)
    return data

a = getdata("testdata.csv")
print(a[1:])