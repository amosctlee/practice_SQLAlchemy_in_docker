"""
two kind of update operations
    Updating ORM Objects: 
        after update the object, we have to call session.flush() method
        or emit any SELECT make it autoflush
    ORM-enabled UPDATE statements:
        no need to flush or emit a SELLECT
"""


from defining_table_metadata_with_the_ORM import User, Address
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:example@mysql_db/testwithsqlalchemy")
session = Session(engine)

# Updating ORM Objects
from sqlalchemy import select
ehkrabs = session.execute(select(User).filter_by(name="ehkrabs")).scalar_one()
print("--- select an object ---")
print(ehkrabs)
print(session.dirty)


ehkrabs.fullname = "Sandy Squirrel"
print("--- update the object ---")
print(session.dirty)
print(ehkrabs in session.dirty)
# session.flush()  manually flush
# print(ehkrabs in session.dirty)

"""
 a flush occurs automatically before we emit any SELECT, 
 using a behavior known as autoflush. We can query directly 
 for the User.fullname column from this row and we will get 
 our updated value back:
"""
sandy_fullname = session.execute(
    select(User.fullname).where(User.id == 18)
).scalar_one()
print("--- emit SELECT make it auto flush ---")
print(sandy_fullname)
print(ehkrabs)
print(ehkrabs in session.dirty)


# ORM-enabled UPDATE statements
from sqlalchemy import select, update
session.execute(
    update(User).
    where(User.name == "ehkrabs").
    values(fullname="Sandy Squirrel Extraodinaire")
)
print("--- ORM-enabled UPDATE statements ---")
print(ehkrabs)

# Rolling Back
session.rollback()
print("--- session rollback ---")
# print(ehkrabs)  # 當我們印出來時，他就執行了查詢，故將此行註解，觀察 __dict__ 結果
print(ehkrabs.__dict__)
print(ehkrabs.fullname)
print(ehkrabs.__dict__)






# session.commit()
