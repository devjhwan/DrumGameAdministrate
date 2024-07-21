from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)

	player_settings = relationship("PlayerSettings", back_populates="user", uselist=False)
