from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

"""
    Registering Tables in the database
"""

from.user_model import User # Importing the User table
from .stickynotes_model import StickyNotes