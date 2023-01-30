from config import db

# class name should be in Pascal case of file name
class User(db.Model):
    __tablename__ = 'user'  #tablename and file name should be same
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    
    projects =db.relationship('Projects', backref='user')
    skills =db.relationship('Skills', backref='user')
    experiences =db.relationship('Experiences', backref='user')
    personal_details = db.relationship('PersonalDetails', backref='user')
    educations = db.relationship('Educations', backref='user')
    certificates = db.relationship('Certificates', backref='user')
    