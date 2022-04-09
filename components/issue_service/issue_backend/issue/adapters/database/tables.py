from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table
)

naming_convention = {
    "all_column_names": lambda constraint, table: "_".join([
        column.name for column in constraint.columns.values()
    ]),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": "fk__%(table_name)s__%(all_column_names)s_%(referred_table_name)s",
    "pk": "pk__%(table_name)s"
}

metadata = MetaData(naming_convention=naming_convention)

issue_table = Table(
    "issues",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=True),
    Column("book_id", Integer, nullable=True),
    Column("action", String(100), nullable=True),
    Column("created_at", DateTime, nullable=True),
)
