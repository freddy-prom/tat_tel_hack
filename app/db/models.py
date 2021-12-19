from sqlalchemy import Column, Integer, String, JSON
from db.database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tatar_word = Column(String)
    russian_word = Column(String)
    tatar_definition = Column(String)
    russian_definition = Column(String)
    transcription = Column(String)
    level = Column(Integer)
    alice_file_id = Column(String)


class Excess(Base):
    __tablename__ = "excess"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(JSON)
    answer = Column(String)
