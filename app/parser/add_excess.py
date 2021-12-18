from db import crud

excesses = [
    {"question": ["көз", "кыш", "гыйнвар", "җәй"], "answer": "гыйнвар", "id": 1},
    {"question": ["кыз", "курчак", "малай", "әни"], "answer": "курчак", "id": 2},
    {"question": ["тәлинкә", "кәстрүл", "урындык", "чәйнек"], "answer": "урындык", "id": 3},
    {"question": ["гөлчәчәк", "төлке", "кыңгырау", "лалә"], "answer": "төлке", "id": 4},
    {"question": ["тавык", "сыер", "сарык", "ат"], "answer": "тавык", "id": 5},
    {"question": ["букча", "китап", "дәфтәр", "блоклык"], "answer": "букча", "id": 6},
    {"question": ["чыпчык", "карлыгач", "карга", "шөпшә"], "answer": "шөпшә", "id": 7},
    {"question": ["сөт", "чәй", "су", "икмәк"], "answer": "икмәк", "id": 8},
    {"question": ["карбыз", "кара", "кура", "алма"], "answer": "алма", "id": 9},
    {"question": ["туп", "даирә", "тартма", "баш"], "answer": "тартма", "id": 10}
]

for excess in excesses:
    crud.add_excess(question=excess["question"],
                    answer=excess["answer"])
