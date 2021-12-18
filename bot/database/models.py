from sqlalchemy import Column, Integer, String
from database.database import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_instance = Column(Integer, nullable=False)
    game_short_name = Column(String, nullable=False)
    inline_query = Column(Integer, nullable=False)
