from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def website():
    """De homepagina van de website

    :return: HTML pagina met een overzicht van de website
    """
    # Returnen van HTML pagina
    return render_template("ninom-html/about.html")


if __name__ == '__main__':
    app.run()