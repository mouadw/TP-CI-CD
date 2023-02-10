from flask import Flask
from flask import request
import sys
import csv
from flask import jsonify

#Création de notre application flask
app = Flask(__name__)





#fonction main de notre projet qui permet d'executer notre Flask apllication.
if __name__ == "__main__":
    if len(sys.argv) > 1 :
        if sys.argv[1] == "check_syntax":
            print("Build [ OK ]")
            exit(0)
        else:
            print("Passed argument not supported ! Supported argument : check_syntax")
            exit(1)
    app.run(debug=True)
