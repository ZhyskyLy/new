from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('Sitio/index.html')

@app.route('/Nosotros')
def Nosotros():
    return render_template('Sitio/Nosotros.html')

@app.route('/Servicios')
def Servicios():
    return render_template('Sitio/Servicios.html')

@app.route('/Contacto')
def Contacto():
    return render_template('Sitio/Contacto.html')


if __name__ =='__main__':
    app.run(debug=True)
    