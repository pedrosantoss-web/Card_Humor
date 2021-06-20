from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    nome = 'HULK'
    humor = True
    imagem1 = "https://media.tenor.com/images/ce9675855b927995d26dfbc20854d757/tenor.gif"
    imagem2 = "https://thumbs.gfycat.com/BeneficialRewardingBison-max-1mb.gif"
    bemhumorado = 'De Boa'
    mauhumorado = 'Estressado'
    return render_template(
        "index.html",
        nome = nome,
        humor = humor,
        imagem1 = imagem1,
        imagem2 = imagem2,
        bemhumorado = bemhumorado,
        mauhumorado = mauhumorado,
    )

if __name__ == "__main__":
    app.run(debug=True)   
