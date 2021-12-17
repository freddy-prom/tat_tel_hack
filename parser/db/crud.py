from db.database import SessionLocal
from db.models import Word
from typing import List


def add_word(russian_word: str) -> Word:
    session = SessionLocal()
    db_word = Word(russian_word=russian_word)
    session.add(db_word)
    session.commit()
    session.refresh(db_word)
    return db_word


def get_russian_words() -> List[str]:
    session = SessionLocal()
    return [_[0] for _ in session.query(Word.russian_word).all()]


def get_words() -> List[Word]:
    session = SessionLocal()
    return session.query(Word).all()


def set_translation(word_id: int, tatar_word: str):
    session = SessionLocal()
    db_word = session.query(Word).filter_by(id=word_id)
    db_word.update({"tatar_word": tatar_word})
    session.commit()


def delete_words():
    session = SessionLocal()
    session.query(Word).delete()
    session.commit()


def delete_word(word_id: int):
    session = SessionLocal()
    session.query(Word).filter(Word.id == word_id).delete()
    session.commit()
