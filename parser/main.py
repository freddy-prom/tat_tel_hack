from db import models, database, crud

models.Base.metadata.create_all(bind=database.engine)
db = database.SessionLocal()

words = crud.get_russian_words()
print(len(words))
