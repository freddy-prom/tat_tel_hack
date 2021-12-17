from sqlalchemy import (Column, Table, String, Integer, MetaData, JSON)

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

words = Table(
    "words",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("tatar_word", String, nullable=False),
    Column("russian_word", String, nullable=False),
    Column("tatar_definition", String, nullable=False),
    Column("russian_definition", String),
    Column("transcription", String, nullable=False),
    Column("level", Integer, nullable=False)
)

find_excess = Table(
    "find_excess",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("task", JSON, nullable=False),
    Column("answer", String, nullable=False),
    Column("level", Integer, nullable=False)
)
