from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
    pass

def add_applicant(id, name, age, subject):
    student_object = Student(
    	id=id,
        name=name,
        age=age,
        subject=subject)
    session.add(applicant_object)
    session.commit()


def query_all():
   applicants = session.query(
      Applicant).all()
   return applicants