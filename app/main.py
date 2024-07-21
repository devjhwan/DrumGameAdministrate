from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import *
from .schemas import UserCreate, User as UserSchema
from .schemas import SongCreate, Song as SongSchema
from .schemas import PlayerSettingsCreate, PlayerSettings as PlayerSettingsSchema
from .schemas import GameResultCreate, GameResult as GameResultSchema

app = FastAPI()

@app.on_event("startup")
def startup():
	from .models import Base
	Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
	db_user = db.query(User).filter(User.email == user.email).first()
	if db_user:
		raise HTTPException(status_code=400, detail="Email already registered")
	hashed_password = user.password + "notreallyhashed"  # 비밀번호 해싱 필요
	db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

@app.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
	db_user = db.query(User).filter(User.id == user_id).first()
	if db_user is None:
		raise HTTPException(status_code=404, detail="User not found")
	return db_user

@app.post("/song/", response_model=SongSchema)
def create_song(song: SongCreate, db: Session = Depends(get_db)):
	db_song = Song(name=song.song_name, list=song.list, level=song.level)
	db.add(db_song)
	db.commit()
	db.refresh(db_song)
	return db_song

@app.get("/song/{song_id}", response_model=SongSchema)
def read_song(song_id: int, db: Session = Depends(get_db)):
	db_song = db.query(Song).filter(Song.id == song_id).first()
	if db_song is None:
		raise HTTPException(status_code=404, detail="Song not found")
	return db_song

@app.post("/player_settings/", response_model=PlayerSettingsSchema)
def create_player_settings(player_settings: PlayerSettingsCreate, db: Session = Depends(get_db)):
	db_player_settings = PlayerSettings(**player_settings.model_dump())
	db.add(db_player_settings)
	db.commit()
	db.refresh(db_player_settings)
	return db_player_settings

@app.get("/player_settings/{user_id}", response_model=PlayerSettingsSchema)
def read_player_settings(user_id: int, db: Session = Depends(get_db)):
	db_player_settings = db.query(PlayerSettings).filter(PlayerSettings.user_id == user_id).first()
	if db_player_settings is None:
		raise HTTPException(status_code=404, detail="PlayerSettings not found")
	return db_player_settings

@app.post("/game_result/", response_model=GameResultSchema)
def create_game_result(game_result: GameResultCreate, db: Session = Depends(get_db)):
	db_game_result = PlayerSettings(**game_result.model_dump())
	db.add(db_game_result)
	db.commit()
	db.refresh(db_game_result)
	return db_game_result



@app.get("/db_game_result/{game_result_id}", response_model=GameResultSchema)
def read_game_result(game_result_id: int, db: Session = Depends(get_db)):
	db_game_result = db.query(GameResult).filter(GameResult.id == game_result_id).first()
	if db_game_result is None:
		raise HTTPException(status_code=404, detail="GameResult not found")
	return db_game_result