from flask import Flask

#create simple flask application
app = Flask(__name__)


if __name__=="__main__":
    app.run(debug=True)
