from sqlalchemy import Column, Integer, String
from ..database import Base

class Song(Base):
	__tablename__ = 'song_table'

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
	list = Column(String)
	level = Column(String)
