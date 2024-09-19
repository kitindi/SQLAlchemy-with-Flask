from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobportal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Define the Employer model
class Employer(db.Model):
    __tablename__ = 'employers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100))
    
    # One-to-many relationship with JobPost
    job_posts = db.relationship('JobPost', backref='employer', lazy=True)

# Define the JobPost model
class JobPost(db.Model):
    __tablename__ = 'job_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Integer)
    
    # Foreign key to the Employer table
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Example route to test adding data
@app.route('/add-employer-job')
def add_employer_job():
    # Create an example employer
    employer = Employer(name='TechCorp', industry='Technology')
    
    # Create job posts for the employer
    job1 = JobPost(title='Software Engineer', description='Develop web applications', salary=60000, employer=employer)
    job2 = JobPost(title='Data Analyst', description='Analyze business data', salary=50000, employer=employer)
    
    # Add employer and job posts to the session
    db.session.add(employer)
    db.session.add(job1)
    db.session.add(job2)
    
    # Commit the changes to the database
    db.session.commit()
    
    return 'Employer and jobs added!'

if __name__ == '__main__':
    app.run(debug=True)
