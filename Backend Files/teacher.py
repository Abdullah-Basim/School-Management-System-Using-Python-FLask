from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from Users import Users
from database import create_app

app,db = create_app()

class Teacher(Users, db.Model):
    __tablename__ = 'teacher'

    sno = db.Column(db.Integer)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    contact_number = db.Column(db.String(15), nullable=True)
    teaching_class = db.Column(db.String(50), nullable=False)
    qualifications = db.Column(db.String(255), nullable=False)
    courses = db.Column(db.String(255), nullable=True)
    meetings = db.Column(db.String(255), nullable=True)

    def __init__(self, name=None, section=None, qualifications=None, phone_number=None,username=None, password=None, email=None):
        self.name = name
        self.section = section
        self.qualifications = qualifications
        self.phone_number = phone_number
        super().__init__(name, username, password, email, phone_number)
        self.tablename='teacher'



    def setName(self, name):
        self.name = name

    def setSection(self, section):
        self.section = section

    def setQualifications(self, qualifications):
        self.qualifications = qualifications

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    def getName(self):
        return self.name

    def getSection(self):
        return self.section

    def getQualifications(self):
        return self.qualifications

    def getPhoneNumber(self):
        return self.phone_number

    def assignCourse(self, course):
        # Assuming Course class has a teacher_id foreign key
        course.teacher_id = self.id
        db.session.commit()

    def viewStudentDetails(self, student):
        # Assuming Student class has a method to retrieve details
        return student.getDetails()

    def Login(self):             
        try:

            if not db.session.is_active:        #In Case if database session is active or localhost is not working
                print("Database connection is not active.")
                return False
            
            #generating SQL query
            
            query = db.session.query(self.__class__).filter(self.__class__.username==self.user_name, self.__class__.password==self.user_password)
            found = query.first()  #executes the generated sql query
            db.session.close()
        except Exception as e:
            print(f"Exception caught: {e}")
            found = None  # Set found to None in case of an exception

        finally:
            if found:
                print('Teacher found')
                return True , found
            else:
                print('Teacher not found')
        return False