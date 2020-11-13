"""
two kind of delete operations
    Deleting ORM Objects:
        after delete the object, we have to call session.flush() method
        or emit any SELECT make it autoflush
    ORM-enabled DELETE Statements:
        no need to flush or emit a SELLECT
"""

from defining_table_metadata_with_the_ORM import User, Address

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, delete
engine = create_engine("mysql+pymysql://root:example@mysql_db/testwithsqlalchemy")
session = Session(engine)

squidward = session.get(User, 17)
print(squidward)

# Deleting ORM Objects
"""
If we mark patrick for deletion, 
as is the case with other operations, 
nothing actually happens yet until a flush proceeds:
"""
# session.delete(squidward)
# print(squidward in session)

"""
Current ORM behavior is that patrick stays in the 
Session until the flush proceeds, which as mentioned 
before occurs if we emit a query:
"""
# print(
#     session.execute(select(User).where(User.name == "squidward")).first()
# )
# print(squidward in session)


# ORM-enabled DELETE Statements
print("--- ORM-enabled DELETE Statements ---")
print(squidward in session)
session.execute(delete(User).where(User.name == "squidward"))
print(squidward in session)

# Rolling Back
session.rollback()

print("--- after rollback ---")
print(squidward in session)

# Closing a Session
session.close()
