from flask import *

app = Flask(__name__)


@app.route('/other')
@app.route('/other/<int:number>')
def Reg(number=None):
    return render_template('other.html', number=number)


@app.route('/')
def home():
    ages = {"Naeemah": 25, "Godwin": 26, "Thapelo": 47, "Jason": 23}
    return render_template('student.html', ages=ages)


if __name__ == '__main__':
    app.run(debug=True)
