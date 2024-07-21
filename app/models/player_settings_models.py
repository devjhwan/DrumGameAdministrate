from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class PlayerSettings(Base):
	__tablename__ = 'player_settings_table'

	user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
	file_path = Column(String)
	all_sound = Column(Float)
	demo_sound = Column(Float)
	bgm_sound = Column(Float)
	video_sound = Column(Float)
	midi_sound = Column(Float)
	effect_sound = Column(Float)
	example_sound = Column(Float)
	sync = Column(Integer)
	is_demo = Column(Boolean)
	is_trot_loop = Column(Boolean)

	user = relationship("User", back_populates="player_settings")
