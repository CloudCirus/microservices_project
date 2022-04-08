from sqlalchemy import Column, Integer, MetaData, String, Table

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

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(100), nullable=True),
    Column("status", String(100), nullable=True),
    Column("name", String(100), nullable=True),
    Column("surname", String(100), nullable=True),
)
