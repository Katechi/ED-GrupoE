from flask import Flask, render_template,request
import pymysql

app = Flask(__name__)


@app.route('/')
def template():
    return render_template('index.html')

@app.route('/carga',methods=['POST'])
def carga():
    usuario = request.form.get("id")
    def carga2 ():
        conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "", db = "csv_db 8")
        cursor = conn.cursor() 
        cursor.execute("SELECT lat,lon,fecha FROM rutas WHERE id = %s ORDER BY fecha, hora;", (usuario))
        ltln=[]
        for item in cursor:
            lat=item[0]
            lon=item[1]
            ltln.append([lat,lon])
            fecha=item[2]
        print("latitud y lon",ltln ,"fecha",fecha)
        return ltln , fecha
    ltln, fecha=carga2()
    return render_template('index.html',ltln=ltln, fecha=fecha) 

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='127.0.0.1')


