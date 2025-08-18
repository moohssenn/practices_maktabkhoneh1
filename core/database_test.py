from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import Boolean, Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# for postgres or other relational databases
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver:5432/db"
# SQLALCHEMY_DATABASE_URL = "mysql://username:password@localhost/db_name"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False # only for sqlite
}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# create base class for declaring tables
Base = declarative_base()




class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    first_name = Column(String(30))
    last_name = Column(String(40),nullable=True)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    is_verified= Column(Boolean, default=True)
 

    def __repr__(self) :
        return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"


# to create tables and database
Base.metadata.create_all(engine)

session = SessionLocal()

# inserting data
"""
ali = User(first_name="ali",age=31)
session.add(ali)
session.commit()
"""


# bulk insert 
"""
mohsen = User(first_name="mohsen",age=40)
saeid = User(first_name="saeid",age=3)
users = [mohsen,saeid]
session.add_all(users)
session.commit()
"""

# retrive all data
# users= session.query(User).all()
# print(users)

# retrive data with filter 

#user = session.query(User).filter_by(first_name="mohsen").all()
#user= session.query(User).filter_by(first_name="mohsen").first()
#users= session.query(User).filter_by(first_name="mohsen").one_or_none()
#print(user)


# Updating a record of data
#user.last_name = "Kouzehgaran"
#session.commit()
#print(user)

# Delet a record of data
"""
if user: 
    session.delete(user)
    session.commit()
"""
# query all users with age greater than or equal to 3
users_all = session.query(User).all()

users_filtered = session.query(User).filter(User.age >=3).all()
print("ALL Users: ", len(users_all))
print("Filtered Users: ", len(users_filtered ))

# add multiple filters
# query all users with age greater than or equal to 25 and name equals to something
users_filtered = session.query(User).filter(User.age >=25,User.first_name == "ali").all()

# or you can use where
users_filtered = session.query(User).where(User.age >=25,User.first_name == "ali").all()

# users with similar name contianing specific substrings
users_similar_name = session.query(User).filter(User.first_name.like("%ali%")).all()

# users with case insensitive match
users_similar_name = session.query(User).filter(User.first_name.ilike("%ali%")).all()

# users with starting and ending chars
users_starting_ali = session.query(User).filter(User.first_name.like("Ali%")).all()
users_ending_ali = session.query(User).filter(User.first_name.like("%Ali")).all()






