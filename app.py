from flask import Flask, request, redirect, url_for, render_template
from sqlalchemy.orm import sessionmaker
from models import Produto
from db import engine

app = Flask(__name__)
Session = sessionmaker(bind=engine)

@app.route("/produtos")
def listar_produtos():
    session = Session()
    produtos = session.query(Produto).all()
    return render_template("produtos.html", produtos=produtos)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == "POST":
        session = Session()
        novo_produto = Produto(
            nome=request.form["nome"],
            categoria=request.form["categoria"],
            tamanho=request.form["tamanho"],
            cor=request.form["cor"],
            quantidade=int(request.form["quantidade"])
        )
        session.add(novo_produto)
        session.commit()
        return redirect(url_for("listar_produtos"))

    produto_vazio = Produto(nome="", categoria="", tamanho="", cor="", quantidade=0)
    return render_template("formulario.html", titulo="Cadastrar Produto", produto=produto_vazio)

@app.route("/excluir/<int:id>")
def escluir_produto(id):
    session = Session()
    produto = session.query(Produto).get(id)

    if produto:
        session.delete(produto)
        session.commit()
        return redirect(url_for("listar_produtos"))
    else:
        return f"<h1>Produto com ID {id} não encontrado. </h1>"

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    session = Session()
    produto = session.query(Produto).get(id)

    if not produto:
        return f"<h1>Produto com ID {id} não encontrado. </h1>"
    
    if request.method == "POST":
        produto.nome = request.form["nome"]
        produto.categoria = request.form["categoria"]
        produto.tamanho = request.form["tamanho"]
        produto.cor = request.form["cor"]
        produto.quantidade = int(request.form["quantidade"])
        session.commit()
        return redirect(url_for("listar_produtos"))
    return render_template("formulario.html", titulo="Editar Produto", produto=produto)
if __name__ == "__main__":
    app.run(debug=True)