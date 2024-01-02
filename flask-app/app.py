from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Booking {self.date} at {self.time} for {self.number_of_people} people>"

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        time = datetime.strptime(request.form['time'], '%H:%M').time()
        number_of_people = int(request.form['number_of_people'])

        if Booking.query.filter_by(date=date, time=time).first():
            return "This slot is already booked", 400

        if number_of_people < 1 or number_of_people > 24:
            return "Invalid number of people", 400

        new_booking = Booking(date=date, time=time, number_of_people=number_of_people)
        db.session.add(new_booking)
        db.session.commit()

        return redirect(url_for('data'))

    return render_template('book.html')

@app.route("/info")
def data():
    bookings = Booking.query.all()
    return render_template('info.html', bookings=bookings)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
