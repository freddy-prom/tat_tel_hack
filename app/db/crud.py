from db.database import SessionLocal
from db.models import Word, Excess
from typing import List


def add_word(russian_word: str) -> Word:
    session = SessionLocal()
    db_word = Word(russian_word=russian_word)
    session.add(db_word)
    session.commit()
    session.refresh(db_word)
    return db_word


def add_complete_word(word_id, tatar_word, russian_word, definition, level) -> Word:
    session = SessionLocal()
    db_word = Word(id=word_id,
                   tatar_word=tatar_word,
                   russian_word=russian_word,
                   definition=definition,
                   level=level)
    session.add(db_word)
    session.commit()
    session.refresh(db_word)
    return db_word


def add_excess(question, answer) -> Word:
    session = SessionLocal()
    db_word = Excess(question=question,
                     answer=answer)
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


def get_word(word_id) -> dict:
    session = SessionLocal()
    word = session.query(Word).filter(Word.id == word_id).first()
    return word_to_json(word) if word else None


def get_words_by_level(level: int) -> List[dict]:
    session = SessionLocal()

    words = session.query(Word).filter(Word.level == level, Word.alice_file_id is not None).all()
    answer = []
    for word in words:
        answer.append(word_to_json(word))

    return answer


def get_all_excesses():
    session = SessionLocal()

    words = session.query(Excess).all()
    answer = []
    for word in words:
        answer.append(excess_to_json(word))

    return answer


def word_to_json(word: Word):
    return {
        "id": word.id,
        "russian_word": word.russian_word,
        "tatar_word": word.tatar_word,
        "definition": word.russian_definition,
        "level": word.level,
    }


def excess_to_json(excess: Excess):
    return {
        "id": excess.id,
        "question": excess.question,
        "answer": excess.answer
    }
