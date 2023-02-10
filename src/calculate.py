from flask import Flask
from flask import request
import sys

#Création de notre application flask
app = Flask(__name__)

class Number :
    def __init__(self, number, id_number):
        self.number = number
        self.id_unumber = id_number
    
    def addition(number1,number2):
        return number1 + number2
    
    def subsrtaction(number1, number2):
        return number1 - number2
    
    def multiplication(number1, number2):
        return number1*number2
    
    def division(number1, number2):
        if number2 != 0:
            return number1/number2
        else : print("error!")

        
number1 = Number(5, 1)
number2 = Number(1, 2)




app.route('/', methods=['GET'])
def index():
    print("addition(number1, number2)")

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
