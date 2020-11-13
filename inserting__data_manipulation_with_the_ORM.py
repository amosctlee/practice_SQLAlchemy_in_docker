from defining_table_metadata_with_the_ORM import User, Address

# Instances of Classes represent Rows
squidward = User(name="squidward", fullname="Squidward Tentacles")
krabs = User(name="ehkrabs", fullname="Eugene H. Krabs")

print(squidward)

# Adding objects to a Session
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:example@mysql_db/testwithsqlalchemy")
session = Session(engine)

"""
The objects are then added to the Session using the Session.add() method. 
When this is called, the objects are in a state known as pending and have 
not been inserted yet:
"""
session.add(squidward)
session.add(krabs)

"""
When we have pending objects, we can see this state by looking at a collection 
on the Session called Session.new:
"""
print(session.new)

# Flushing
"""
The Session makes use of a pattern known as unit of work. 
This generally means it accumulates changes one at a time, 
but does not actually communicate them to the database until needed.

When it does emit SQL to the database to push out the current set of changes, 
the process is known as a flush.
"""
session.flush()

print(squidward)
print(krabs)
print(session.new)

# Committing
session.commit()
