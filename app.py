from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/Nosotros')
def Nosotros():
    return render_template('sitio/Nosotros.html')

@app.route('/Servicios')
def Servicios():
    return render_template('sitio/Servicios.html')

@app.route('/Contacto')
def Contacto():
    return render_template('sitio/Contacto.html')


if __name__ =='__main__':
    app.run(debug=True)
    