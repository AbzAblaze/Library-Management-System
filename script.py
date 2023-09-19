#Import Modules
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Base Class that all classes inherit from.
Base = declarative_base()

#Class=Table in SQLAlchemy
class Person(Base):
	__tablename__ = 'persons'
	#Columns
	pid = Column("pid", Integer, primary_key=True)
	first_name = Column("firstname", String)
	last_name = Column("lastname", String)
	gender = Column("gender", String)
	age = Column("age", Integer)
	#Constructor
	def __init__(self, pid, first, last, gender, age):
		self.pid = pid
		self.first_name = first
		self.last_name = last
		self.gender = gender
		self.age = age
	#String Representation
	def __repr__(self):
		return f"({self.pid} {self.first_name} {self.last_name} {self.gender} {self.age})"
	
#Class=Table in SQLAlchemy
class Thing(Base):
	__tablename__ = 'things'
	#Columns
	tid = Column("tid", Integer, primary_key=True)
	description = Column("description", String)
	owner = Column(Integer, ForeignKey("persons.pid"))
	#Constructor
	def __init__(self, tid, description, owner):
		self.tid = tid
		self.description = description 
		self.owner = owner
	#String Representation
	def __repr__(self):
		return f"({self.tid}, {self.description} owned by {self.owner})"

#Create Engine (Connects to SQL DB)
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine) #Takes all classes that extend from base and creates in DB.	
#Session
Session = sessionmaker(bind=engine)
session = Session()

#Create Persons
p1 = Person(238, "Martin", "Drake", "Male", 32)
session.add(p1)
p2 = Person(485, "Jenny", "Smith", "Female", 25)
session.add(p2)
p3 = Person(716, "Jason", "Maroon", "Male", 19)
session.add(p3)
#Create Things
t1 = Thing(12, 'Book', p1.pid)
session.add(t1)
t2 = Thing(32, 'Phone', p2.pid)
session.add(t2)
t3 = Thing(52, 'Pen', p3.pid)
session.add(t3)
#Commit
session.commit()

#Query Filter
results = session.query(Person, Thing).filter(Thing.owner == Person.pid).filter(Person.first_name == 'Martin').all()
print(results)