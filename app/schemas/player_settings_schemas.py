from pydantic import BaseModel
from .user_schemas import User

class PlayerSettingsBase(BaseModel):
	user_id: int
	file_path: str
	all_sound: float
	demo_sound: float
	bgm_sound: float
	video_sound: float
	midi_sound: float
	effect_sound: float
	example_sound: float
	sync: int
	is_demo: bool
	is_trot_loop: bool

class PlayerSettingsCreate(PlayerSettingsBase):
	user_id: int

class PlayerSettings(PlayerSettingsBase):
	user_id: int
	user: User

	class Config:
		from_attributes = True