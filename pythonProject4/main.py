from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def formcompras():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        valor = tarros * 9000
        resultado = 0
        descuento = 0
        if edad >= 18 and edad <= 30:
            descuento = valor * 0.15
            resultado = valor-descuento
        elif edad >30:
            descuento = valor * 0.25
            resultado = valor - descuento
        return render_template('ejercicio1.html', resultado=resultado, nombre=nombre, edad=edad, tarros=tarros, valor=valor, descuento=descuento)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def formclave():
    if request.method == 'POST':
        juan = 'juan'
        clave1 = 'admin'
        pepe = 'pepe'
        clave2 = 'user'
        usuario = str(request.form['usuario'])
        password = str(request.form['password'])
        resultado = ''
        if usuario == juan and password == clave1:
            resultado = 'Bienvenido administrador Juan'
        elif usuario == pepe and password == clave2:
            resultado = 'Bienvenido usuario pepe'
        else:
            resultado = ' Usuario o contraseña incorrectas'
        return render_template('ejercicio2.html',usuario=usuario, password=password, resultado=resultado)
    return render_template('ejercicio2.html')
if __name__ == '__main__':
    app.run(debug=True)