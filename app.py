from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/captura", methods=["POST"])
def captura():
    nome = request.form.get("nome")
    telefone = request.form.get("telefone")

    con = sqlite3.connect("leads.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS leads (nome TEXT, telefone TEXT)")
    cur.execute("INSERT INTO leads (nome, telefone) VALUES (?, ?)", (nome, telefone))
    con.commit()
    con.close()

    return "Acesso liberado! Você será redirecionado para a internet."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
