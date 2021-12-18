from sqlalchemy import Column, Integer, String
from parser.db.database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tatar_word = Column(String)
    russian_word = Column(String)
    tatar_definition = Column(String)
    russian_definition = Column(String)
    transcription = Column(String)
    level = Column(Integer)
