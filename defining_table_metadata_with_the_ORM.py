"""
step:
1. create Base class: there are two way to create it.
2. declaring Mapped Classes
3. Emitting DDL to the database: there are two way to create it.

"""

# Setting up the Registry
from sqlalchemy.orm import registry
"""
When using the ORM, the MetaData collection remains present, 
however it itself is contained within an ORM-only object known as the registry.
"""
mapper_registry = registry()
# print(mapper_registry.metadata)

"""
Instead of declaring Table objects directly,
we will now declare them indirectly through directives applied to our mapped classes. 
In the most common approach, each mapped class descends from a common base class known as the declarative base.
"""
Base = mapper_registry.generate_base()

""" Tip
The steps of creating the registry and “declarative base” classes can be 
combined into one step using the historically familiar declarative_base() function:

# from sqlalchemy.orm import declarative_base
# Base = declarative_base()
"""

# Declaring Mapped Classes
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(100))

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}"


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# print(User.__table__)
# print(User)


# Emitting DDL to the database
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:example@mysql_db/testwithsqlalchemy")

# # emit CREATE statements given ORM registry
# mapper_registry.metadata.create_all(engine)

# the identical MetaData object is also present on the declarative base
Base.metadata.create_all(engine)
