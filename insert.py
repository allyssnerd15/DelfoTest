from views import assets_create, measurementservice_create

import csv

def read_arq():
    lista = []
    with open(f'C:\\Users\\Rafaeel Meira Dantas\\OneDrive\\Documentos\\DelfoTest\\arquivo\\measurements.csv', mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            lista.append(row)
            
    return lista

def main():
    response = read_arq()
    for item in response:
        import pdb; pdb.set_trace()
        assets_create(item[0], item[1])

if __name__=='__main__':
    resp = main()
