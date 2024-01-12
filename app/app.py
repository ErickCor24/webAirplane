from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/registro')
def registro():
    return render_template('Registro_boleto.html')

@app.route('/vuelo')
def vuelo():
    return render_template('crear_vuelo.html')


@app.route('/flight')
def flight():
    return render_template('crear_vuelo.html')

@app.route('/boleto')
def boleto():
    return render_template('Registro_boleto.html')

@app.route("/pago")
def pago():
    return render_template('registro_pago.html')

if __name__ == '__main__':
    app.run(debug=True)

