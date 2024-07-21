from pydantic import BaseModel

class SongBase(BaseModel):
	song_name: str
	list: str
	level: str

class SongCreate(SongBase):
	pass

class Song(SongBase):
	id: int

	class Config:
		from_attributes = True