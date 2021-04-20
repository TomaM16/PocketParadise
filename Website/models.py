import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, aliased
from sqlalchemy.sql.expression import func

from database import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    login_id = Column(String(36), nullable=True)
    # topic = relationship('topic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.login_id

    def __repr__(self):
        return '<User %r>' % self.username


class Tag:
    __tablename__ = 'Tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    color = Column(String(6), unique=True, nullable=False)


class Question(Base):
    __tablename__ = 'Question'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    likes = Column(Integer, unique=False, nullable=True)
    seens = Column(Integer, unique=False, nullable=True)
    is_solved = Column(Boolean, unique=False, nullable=False, default=False)


class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))
