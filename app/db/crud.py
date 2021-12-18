from parser.db.database import SessionLocal
from parser.db.models import Word
from typing import List


def add_word(russian_word: str) -> Word:
    session = SessionLocal()
    db_word = Word(russian_word=russian_word)
    session.add(db_word)
    session.commit()
    session.refresh(db_word)
    return db_word


def get_words() -> List[dict]:
    session = SessionLocal()

    words = session.query(Word).all()
    answer = []
    for word in words:
        answer.append(word_to_json(word))

    return answer


def get_words_by_level(level: int) -> List[dict]:
    session = SessionLocal()

    words = session.query(Word).filter(Word.level == level).all()
    answer = []
    for word in words:
        answer.append(word_to_json(word))

    return answer


def word_to_json(word: Word):
    return {
        "id": word.id,
        "russian_word": word.russian_word,
        "tatar_word": word.tatar_word,
        "definition": word.tatar_definition,
        "level": word.level,
    }
