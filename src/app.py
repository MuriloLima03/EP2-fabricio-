from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("teste2.html")
    
@app.route("/contato")
def contato():
    return render_template("contato2.html")

@app.route("/projetos")
def quemsomos():
    return render_template("projetos2.html")
    
@app.route("/peixes")
def peixes():
    return render_template("/templates/peixe/index.html")

if __name__ == "__main__":
    app.run(debug=True)