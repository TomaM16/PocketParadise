import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, aliased
from sqlalchemy.sql.expression import func

from database import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    login_id = Column(String(36), nullable=True)

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
