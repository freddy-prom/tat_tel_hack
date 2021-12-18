from typing import TypedDict


class Word(TypedDict):
    id: str
    tatar_word: str
    russian_word: str
    definition: str
    level: int
