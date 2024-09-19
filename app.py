from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
import uuid


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
      
      
    
# create a sqlite database connection

db = "sqlite:///socialdb.db"
engine = create_engine(db)

# create tables for social database
Base.metadata.create_all(bind=engine)


# create session for each user to be able to enteract with tables   

Session = sessionmaker(bind=engine)
session = Session()


# create user

firstName = "kitindi"
lastName = "Tech"
profileName ="dax"
email = "daxtech@gmail.com"

user = users(firstName, lastName, profileName, email)

session.add(user) #staging are
session.commit()

# create a post

userID = ""
postContent ="Nice course"

newPost = posts(userID, postContent)
session.add(newPost)
session.commit()