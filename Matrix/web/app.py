from flask import *
import sympy

app = Flask(__name__)

@app.route('/')
def page_main():
    equations = create_equations()
    return render_template('quest.html', equations=equations)

def create_equations():
    solutions = [9, 6, 2, 3]
    equations = []
    for sol in solutions:
        a = sympy.randprime(1, 100)
        b = sympy.randprime(1, 100)
        c = a * sol + b
        equation = f"{a}x + {b} = {c}"
        equations.append(equation)
    return equations

app.run()