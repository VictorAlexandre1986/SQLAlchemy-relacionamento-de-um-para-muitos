import os
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conn = 'sqlite:///'+os.path.join(BASE_DIR, 'blog.db')

engine = create_engine(conn, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__="users"
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    #posts = relationship('Post', backref='author')
    #Use o de baixo
    posts = relationship('Post', backref='author', cascade='all, delete')
    
    def __repr__(self):
        return f"<User {self.username}>"
    
    
class Post(Base):
    __tablename__="post"
    id = Column(Integer(), primary_key=True)
    title = Column(String(50), nullable = False)
    content = Column(String(400), nullable = False)
    user_id = Column(Integer(), ForeignKey("users.id"))
    
    def __repr__(self):
        return f"<Post {self.title}>"    
    

session = sessionmaker()(bind=engine)

