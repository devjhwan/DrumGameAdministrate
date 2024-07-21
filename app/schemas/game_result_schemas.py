from pydantic import BaseModel

class GameResultBase(BaseModel):
	user_id: int
	song_id: int
	play_date: str
	level: int
	repeat: bool
	score: int
	max_combo: int
	rank: str
	perfect: int
	great: int
	good: int
	bad: int
	miss: int
	strike_rate: float
	total_hit: int
	total_strike: int
	spent_calorie: float

class GameResultCreate(GameResultBase):
	pass

class GameResult(GameResultBase):
	id: int

	class Config:
		from_attributes = True
