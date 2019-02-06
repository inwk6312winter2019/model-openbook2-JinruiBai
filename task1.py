import csv
def tupl():
    tuple = ()
    with open('Street_Centrelines.csv','rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[2] for row in reader]
         tuple = colunm
         colunm = [row[4] for row in reader]
         subtuple = colunm
         tuple = tuple + colunm
         colunm = [row[6] for row in reader]
         tuple = tuple + colunm
         colunm = [row[7] for row in reader]
         tuple = tuple + colunm
    return tuple;

def dictionary():
    dic = dict()
    with open('Street_Centrelines.csv','rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[12] for row in reader]
         dic = {'MAINTENANCE' : colunm}
    return dic

def list():
    list = []
    with open('Street_Centrelines.csv','rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[12] for row in reader]
         list = colunm
    return list

def classfor():
    list_class_street = []
    with open('Street_Centrelines.csv','rb') as fin:
         reader = csv.reader(fin)
         colunm = [row[10] for row in reader]
         list_class_street = colunm
    return list_class_street
