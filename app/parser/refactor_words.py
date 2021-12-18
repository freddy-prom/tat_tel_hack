from app.db import crud


def refactor():
    all_words = crud.get_words()
    res = []
    for word in all_words:
        if word["tatar_word"] and word["russian_word"] not in word["tatar_word"]:
            word["tatar_word"] = remove_spaces(word["tatar_word"])
            word["russian_word"] = remove_spaces(word["russian_word"])
            word['level'] = get_lvl(word["tatar_word"].split(",")[0])
            res.append(word)
    for word in res:
        crud.add_complete_word(word_id=word["id"],
                               tatar_word=word["tatar_word"],
                               russian_word=word["russian_word"],
                               definition=word["definition"],
                               level=word["level"])


def get_lvl(word):
    if len(word) < 5:
        return 1
    elif len(word) < 8:
        return 2
    elif len(word) < 10:
        return 3
    else:
        return 4


def remove_spaces(s: str):
    counter = 0
    s = s.replace("\n", " ")
    s = s.replace("\t", " ")
    for liter in s:
        if liter != " " and counter != 0:
            s = s.replace(" " * counter, " ", 1)
            counter = 0
        elif liter == " ":
            counter += 1
    return s
