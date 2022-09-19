from flask import Flask
import click

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@click.command()
def hello():
    click.echo("Hello, there!")

if __name__ == "__main__":
    hello()
    app.run()