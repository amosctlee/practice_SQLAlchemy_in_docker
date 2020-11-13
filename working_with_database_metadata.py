
# Version Check
"""
import sqlalchemy

print(sqlalchemy.__version__)
"""

# Establishing Connectivity - the Engine
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:example@mysql_db/testwithsqlalchemy")

# Setting up MetaData with Table objects
from sqlalchemy import MetaData
metadata = MetaData()

from sqlalchemy import Table, Column, Integer, String
user_table = Table(
    "user_account",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String(100))
)

print(user_table.c.fullname)
print(user_table.c.keys())
print(user_table.primary_key)

# Declaring Simple Constraints
from sqlalchemy import ForeignKey
address_table = Table(
    "address",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String(250), nullable=False)
)

print(address_table.c)
print(address_table.foreign_keys)


# Emitting DDL to the Database
print(metadata.create_all(engine))

print(metadata.drop_all(engine))
