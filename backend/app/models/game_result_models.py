from sqlalchemy import Column, Integer, String, Float, Boolean
from ..database import Base

class GameResult(Base):
	__tablename__ = 'game_result_table'

	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, index=True)
	song_id = Column(Integer, index=True)
	play_date = Column(String)
	level = Column(Integer)
	repeat = Column(Boolean)
	score = Column(Integer)
	max_combo = Column(Integer)
	rank = Column(String)
	perfect = Column(Integer)
	great = Column(Integer)
	good = Column(Integer)
	bad = Column(Integer)
	miss = Column(Integer)
	strike_rate = Column(Float)
	total_hit = Column(Integer)
	total_strike = Column(Integer)
	spent_calorie = Column(Float)
