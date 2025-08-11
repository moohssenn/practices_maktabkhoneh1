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



# * / model.py



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age=Column(Integer)
    is_active = Column(Boolean, default=True)
    




# to create tables and database
Base.metadata.create_all(engine)
