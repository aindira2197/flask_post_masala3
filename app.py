from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

@app.route('/', methods=["POST", 'GET'])
def index():
    if request.method == 'POST':
        nomi = request.form.get('kitob_nomi')
        muallif = request.form.get('muallif')
        sahifa = request.form.get('sahifalar')

        if len(nomi) > 3 and len(muallif) > 3 and int(sahifa) >= 50:
            res = [nomi, muallif, sahifa]
        else:
            res =  ["Ma'lumotlar noto'g'ri kiritildi"]

        return render_template('info.html', res=res)
    
    return render_template('index.html') 



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
