from flask import Flask, render_template
from database import db, Pickup  # Import SQLAlchemy instance and models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pickup_data')
def pickup_data():
    try:
        pickups = Pickup.query.all()
        return render_template('pupTable.html', pickups=pickups)
    except Exception as e:
        print(f"Error fetching data from database: {str(e)}")
        return f"An error occurred while fetching data: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
