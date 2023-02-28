from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from my_form import MyForm

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = "en un lugar de la mancha"
csrf.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        formulario = MyForm()
        return render_template('index.html', form=formulario)
    else:
        formulario = MyForm(request.form)
        return render_template('index.html', form=formulario)
     
@app.route('/result', methods=['POST'])
def resultado():
    formulario = MyForm(request.form)
    valores = [int(number) for number in formulario.numeros.data]
    
    repetidos = []

    for valor in set(valores):
        repeticiones = len([num for num in valores if num == valor])
        if repeticiones > 1:
            repetidos.append((valor, repeticiones))

    return render_template('result.html', valores=valores, minNum=min(valores), maxNum=max(valores), promedio=sum(valores) / len(valores), repetidos=repetidos)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
