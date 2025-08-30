from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import Column, Integer, String, Float


SQLALCHEMY_DATABASE_URL = "sqlite:///./costs.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False 
}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# create base class for declaring tables
Base = declarative_base()

class Costs(Base):
    __tablename__ = "costs"
   
    id = Column(Integer, primary_key=True,autoincrement=True)
    description = Column(String(45),nullable=False)
    price = Column(Float(10),nullable=False)

# تابع برای گرفتن session از SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
