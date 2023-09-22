#!/usr/bin/python3
# Graham S. Paul (user.py)
"""This module defines a class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models.stringtemplates import HBNB_TYPE_STORAGE, DB
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv(HBNB_TYPE_STORAGE) == DB:
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

     def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, myemail@gmail.com):
        """email values"""
        self._email = myemail@gmail.com

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """hashing password values"""
        self._password = pwd

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, John):
        """first_name values"""
        self._first_name = John

     @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, Doe)
        """last_name values"""
        self._last_name = Doe
