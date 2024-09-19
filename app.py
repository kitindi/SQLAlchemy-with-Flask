from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
import uuid

# Define the SQLite database URL
DATABASE_URL = "sqlite:///socialdb.db"

# Create an engine that connects to the SQLite database
engine = create_engine(DATABASE_URL, echo=True)

# Create a declarative base class to define models
Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())

class users(Base):
    __tablename__ = 'users'
    userID = Column("userID", String, primary_key=True, default=generate_uuid)
    firstName = Column("firstName", String)
    lastName = Column("lastName", String)
    profileName = Column("profileName", String)
    email = Column("email", String)
    
    def __init__(self, firstName, lastName, profileName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.profileName = profileName
        self.email = email


class posts(Base):
    __tablename__ = 'posts'
    postId =Column('postId', String, primary_key=True, default = generate_uuid)
    userID =Column('userID', String, ForeignKey('users.userID'))
    postContent =Column('postContent', String)
    
    def __init__(self, userID, postContent):
      self.userID = userID
      self.postContent = postContent
      


# Create all the tables in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine, future=True)

session = Session()


# function to add user in database


def addUser( firstName, lastName, profileName,email,  session,):
    # chech if the user exists
    
    exist = session.query(users).filter(users.email == email).all()
    
    if len(exist) > 0:
        print("User already exists")
    else:
        user = users(firstName, lastName,profileName, email, )
        session.add(user)
        session.commit()
        print("User added to the database")

# function to add a post to the database

def addPost(userID,postContent,session, ):
    newPost = posts(userID, postContent)
    session.add(newPost)
    session.commit()
    print("Post added to the database")
    

firstName ="Alexander"
lastName ="Johson"
email = "alexjony@gmail.com"
profileName = "alexis"
addUser(firstName, lastName, profileName, email, session)