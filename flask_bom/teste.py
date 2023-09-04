from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(120), unique=False, nullable=False)
    cor = db.Column(db.String(120), unique=False, nullable=False)
    marcamodelo = db.Column(db.String(120), unique=False, nullable=False)
    anodefabricacao = db.Column(db.String(120), unique=False, nullable=False)
    estado = db.Column(db.String(120), unique=False, nullable=False)
    kmrodados = db.Column(db.Integer, unique=False, nullable=False)
    passagem = db.Column(db.String(120), unique=False, nullable=False)
    formapag = db.Column(db.String(120), unique=False, nullable=False)

#CRIAR O BANCO DE DADOS
# with app.app_context():
#     db.create_all()



@app.route("/")
def adicionar():
    return render_template("adicionarveiculo.html")




@app.route('/adicionar_veiculo', methods=['POST'])
def adicionar_veiculo():
    if request.method == 'POST':
        tipo = request.form['tipo']
        cor = request.form['cor']
        marcamodelo = request.form['marcamodelo']
        anodefabricacao = request.form['anodefabricacao']
        estado = request.form['estado']
        kmrodados = request.form['kmrodados']
        passagem = request.form['passagem']
        formapag = request.form['formapag']

        veiculo = Veiculo(tipo=tipo, cor=cor, marcamodelo=marcamodelo, anodefabricacao=anodefabricacao, estado=estado,kmrodados=kmrodados,passagem=passagem,formapag=formapag)
        db.session.add(veiculo)
        db.session.commit()
        veiculos = Veiculo.query.all()  
        return render_template("listarveiculo.html", veiculos=veiculos)



@app.route("/listarveiculo.html")
def listar():
    veiculos = Veiculo.query.all()  
    return render_template('listarveiculo.html', veiculos=veiculos)

@app.route("/excluir.html")
def excluir():
    return render_template("excluir.html", naoexiste = False)

@app.route("/alterarveiculo.html")
def alterar():
   
    return render_template("alterarveiculo.html",  naoexiste = False)

@app.route('/buscar_veiculo', methods=['POST'])
def buscar_veiculo():
    if request.method == 'POST':
        veiculo_id = request.form['veiculo_id']
        veiculo = Veiculo.query.get(veiculo_id)

        if veiculo:
           
            return render_template('alterarveiculo.html',existe = True , veiculo1 =Veiculo.query.get(veiculo_id), naoexiste = False  )
        else:
            return render_template('alterarveiculo.html',naoexiste = True  )

    return redirect(url_for("/listarveiculo.html"))  # Redireciona de volta à página inicial, se necessário

@app.route('/buscar_veiculoExcluir', methods=['POST'])
def buscar_veiculoExcluir():
    if request.method == 'POST':
        veiculo_id = request.form['veiculo_id']
        veiculo = Veiculo.query.get(veiculo_id)

        if veiculo:
           
            return render_template('excluir.html',veiculo1 =Veiculo.query.get(veiculo_id), naoexiste = False, existe = True  )
        else:
            return render_template('excluir.html',naoexiste = True  )

    return redirect(url_for("/listarveiculo.html"))


@app.route('/confirmar_edicao', methods=['POST'])
def confirmar_edicao():
    if request.method == 'POST':
        veiculo_id = request.form['id']
        veiculo = Veiculo.query.get(veiculo_id)

        if veiculo:
            
            veiculo.tipo = request.form['tipo']
            veiculo.cor = request.form['cor']
            veiculo.marcamodelo = request.form['marcamodelo']
            veiculo.anodefabricacao = request.form['anodefabricacao']
            veiculo.estado = request.form['estado']
            veiculo.kmrodados = request.form['kmrodados']
            veiculo.passagem = request.form['passagem']
            veiculo.formapag = request.form['formapag']
        

            db.session.commit() 
            veiculos = Veiculo.query.all()  
            return render_template('listarveiculo.html', veiculos=veiculos)
        else:
            return "Veículo com ID não encontrado."


    veiculos = Veiculo.query.all()  
    return render_template('listarveiculo.html', veiculos=veiculos)



@app.route('/confirmar_exclusao', methods=['POST'])
def confirmar_exclusao():
    if request.method == 'POST':
        veiculo_id = request.form['id']
        veiculo = Veiculo.query.get(veiculo_id)

        if veiculo:
  
           
        
            db.session.delete(veiculo)
            db.session.commit() 
            veiculos = Veiculo.query.all()  
            return render_template('listarveiculo.html', veiculos=veiculos)
        else:
            return "Veículo com ID não encontrado."

if __name__ == "__main__":
    app.run(debug=True)

