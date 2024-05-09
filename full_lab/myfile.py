from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import re



app = Flask('Places of work')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///companies.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
exper = 1


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comp_name = db.Column(db.String(300))
    term = db.Column(db.Integer)
    in_stock = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'Company{self.id}. {self.comp_name} - {self.term} mon.'



@app.route('/')
def main():
    companies = Company.query.all()

    time = 0
    for i in range(len(companies)):
        slice = str(companies[i])
        flag1 = slice.find(' - ') + 3
        flag2 = slice.find(' mon.')
        period = slice[flag1:flag2]
        time += int(period)

    return render_template('my.html', companies_list=companies,
                           experience=time)


@app.route('/add', methods=['POST'])
def add_company():
    data = request.json
    company = Company(**data)
    db.session.add(company)
    db.session.commit()

    return 'OK'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

