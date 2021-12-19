from .all_words import AllWords
from .random_words import RandomWord
from .words_by_level import LevelWords
from .ping import Ping
from .words_by_level_random_count import LevelWordsRandomCount
from .find_exces import FindExcess
from .like_words import LikeWords

handlers = [
    AllWords,
    RandomWord,
    LevelWords,
    Ping,
    LevelWordsRandomCount,
    FindExcess,
    LikeWords
]
