# Creating a backend for a resume generation website 

# Tables in Resume App - 

User    
    - id
    - username


Personal Details
    - id 
    - name
    - phone number
    - email
    - address
    - linkedin_url
    - foreignKey['user.id']


Projects
    - id 
    - name
    - description
    - start_date
    - end_date
    - foreignKey['user.id']


Experiences
    - id
    - company_name
    - role
    - role_description
    - start_date
    - end_date
    - foreignKey['user.id']


Education 
    - id 
    - school_name
    - degree_name
    - start_date
    - end_date
    - foreignKey['user.id']


Skills 
    - id 
    - title
    - confidence_score
    - foreignKey['user.id']


Certificates
    - id 
    - title
    - start_date
    - end_date
    - foreignKey['user.id']
