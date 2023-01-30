from flask import  Flask, request, jsonify
from flask_cors import CORS
from config import db, SECRET_KEY
from os import path, getcwd, environ
from dotenv import load_dotenv
# independent tables are called first
from models.user import User
# dependent tables are called
from models.projects import Projects
from models.experiences import Experiences 
from models.educations import  Educations
from models.skills import Skills
from models.certificates import Certificates
from models.personalDetails import PersonalDetails

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.secret_key = SECRET_KEY


    db.init_app(app)
    print("DB initialized successfully")

    with app.app_context():
        @app.route('/signup', methods=['POST'])
        def signup():
            data = request.form.to_dict(flat=True)

            new_user = User(
                username = data['username']
            )

            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg = "User signed up successfully")


        @app.route('/add_personal_details', methods=['POST'])
        def add_personal_details():
            recv_username = reuest.args.get('username')
            user = User.query.filter_by(username == recv_username).first()

            data = request.get_json()

            new_personal_details = PersonalDetails(
                user_id = user.id,
                name = data['name'],
                email = data['email'],
                number = data['number'],
                address = data['address'],
                linkedin_url = data['linkedin_url'],
            )

            db.session.add(new_personal_details)
            db.session.commit()
            return jsonify(msg = "Personal details added successfully")

        
        @app.route('/add_projects',methods=['POST'])
        def add_projects():
            recv_username = reuest.args.get('username')
            user = User.query.filter_by(username == recv_username).first()

            project_data = request.get_json()

            for data in project_data['data']:
                new_project = Project(
                    name = data['name'],
                    desc = data['desc'],
                    start_date = data['start_date'],
                    end_date = data['end_date'],
                    user_id = user.id
                )

                db.session.add(new_project)
                db.session.commit()
            return jsonify(msg = "Project added successfully")


        @app.route('/add_experiences', methods=['POST'])
        def add_experiences():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username == recv_username).first()

            exp_data = request.get_json()


            for data in exp_data["data"]:
                new_experience = Experiences(
                    user_id = user.id,
                    role = data['role'],
                    role_description = data['role_description'],
                    company_name = data['company_name'],
                    start_date = data['start_date'],
                    end_date = data['end_date']
                )

                db.session.add(new_experience)
                db.session.commit()
            return jsonify(msg = "Experience added successfully")


        @app.route('/add_educations', methods=['POST'])
        def add_educations():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username == recv_username).first()

            edu_data = request.get_json()

            for data in edu_data["data"]:
                new_education = Educations(
                    user_id = user.id,
                    school_name = data['school_name'],
                    degree_name = data['degree_name'],
                    start_date = data['start_date'],
                    end_date = data['end_date']
                )
                
                db.session.add(new_education)
                db.session.commit()

            return jsonify(msg = "Education added successfully")


        @app.route('/add_skills', methods=['POST'])
        def add_skills():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username == recv_username).first()

            skill_data = request.get_json()

            for data in skill_data["data"]:
                new_skill = Skills(
                    user_id = user.id,
                    title = data['title'],
                    confidence_score = data['confidence_score']
                )

                db.session.add(new_skill)
                db.session.commit()

            return jsonify(msg = "Skill added successfully") 


        @app.route('/add_certificates', methods = ['POST'])
        def add_certificates():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username == recv_username).first()

            cert_data = request.get_json()

            for data in cert_data["data"]:
                new_certificate = Certificates(
                    user_id = user.id,
                    title = data['title'],
                    start_date = data['start_date'],
                    end_date = data['end_date']
                )
                
                db.session.add(new_certificate)
                db.session.commit()
            
            return jsonify(msg = "Certificate added successfully")


        @app.route('/get_resume_json', methods = ['GET'])
        def get_resume_json():
            recv_username = request.args.get('username')
            user = User.query.filter_by(username == recv_username).first()

            personal_details = PersonalDetails.query.filter_by(user_id = user.id).first()
            experiences = Experience.query.filter_by(user_id = user.id).all()
            projects = Projects.query.filter_by(user_id = user.id).all()
            educations = Educations.query.filter_by(user_id = user).all()
            skills = Skills.query.filter_by(user_id = user.id).all()
            certificates = Certificates.query.filter_by(user_id = user.id).all()

            resume_data={
                "name" : personal_details.name,
                "email" : personal_details.email,
                "number" : personal_details.number,
                "address" : personal_details.address,
                "linkedin_url" : personal_details.linkedin_url

            }

            experiences_data =[]
            projects_data = []
            educations_data = []
            skills_data = []
            certificates_data = []

            for exp in experiences:
                experiences_data.append({
                    "company_name" : exp.company_name,
                    "role":exp.role,
                    "role_description" : exp.role_description,
                    "start_date": exp.start_date,
                    "end_date": exp.end_date
                    })

            for proj in projects:
                projects_data.append({
                    "name" : proj.name,
                    "desc" : proj.desc,
                    "start_date": proj.start_date,
                    "end_date": proj.end_date
                    })
                
            

            for edu in educations:
                educations_data.append({
                    "school_name": edu.school_name,
                    "degree_name": edu.degree_name,
                    "start_date": edu.start_date,
                    "end_date": edu.end_date
                    })

            for skill in skills:
                skills_data.append({
                    "title": skill.title,
                    "confidence_score": skill.confidence_score
                })

            for cert in certificates:
                certificates_data.append({
                    "title": cert.title,
                    "start_date": cert.start_date,
                    "end_date": cert.end_date
                })


            resume_data["experiences"] = experiences_data
            resume_data["projects"] = projects_data
            resume_data["educations"] = educations_data
            resume_data["skills"] = skills_data
            resume_data["certificates"] = certificates_data

        return resume_data

        # db.drop_all()
        db.create_all()
        db.session.commit()

        return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port='4545', debug=True)