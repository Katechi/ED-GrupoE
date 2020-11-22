from flask import Flask, render_template
import csv

def read_csv_file(filename):
    data = []
    for row in csv.reader(open(filename)):
        data.append(row)
    #print (data)
    return data

def procesar (data):
    x=[0]
    y=[0]
    z=[0] 
    k=[0] 
    for fila in range(1, len(data)):
        x.append(float(data[fila][5]))
        y.append(float(data[fila][6]))
        z.append(float(data[fila][7]))
        k.append(float(data[fila][13]))
    print (y)
    return x,y,z ,k
    


datos         = read_csv_file('uma_02.csv')
x,y,z,k = procesar(datos)


app = Flask(__name__)

@app.route('/')
def template():
    return render_template('index.html',x= x,y = y, z=z , k=k)

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='127.0.0.1')
